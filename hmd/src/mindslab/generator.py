from src.abstract.automata.automata import AbstractAutomata
from src.abstract.automata.automata import AbstractAutomataMachine
from src.abstract.generator.generator import AbstractGenerator
from src.abstract.lexer.lexer import AbstractLexer
from src.abstract.lexer.token import AbstractToken
from src.abstract.parser.parser import AbstractParser
from src.debug import *
from src.mindslab.grammar import HMDGrammar
from src.mindslab.syntax import *
import itertools
import re
import sys

# flatten
# -------
#
# : Recursively flatten nested arrays into single dimensional array.
#
def flatten(arrays=[]):
    '''
    + parameters:
    - {list} arrays -- nested arrays.
    '''
    if not arrays: return []
    elif isinstance(arrays[0], tuple) or isinstance(arrays[0], list):
        return flatten(arrays[0]) + flatten(arrays[1:])
    return arrays[:1] + flatten(arrays[1:])

# permute
# -------
#
# : Get cartesian products of input lists.
#
# TODO: move this outside to function.
#
def permute(self, categories=[], definition=''):
    '''
    + parameters:
    - categories {list} -- a list of categories.
    - definition {list} -- definition.
    '''
    try:
        blocks = definition[1:-1].split(')(')
        assert bool(blocks)
    except AssertionError: raise
    except IndexError: raise

    # tokenize into sets and also remember their index
    s_p, s_q = [], []
    for i, block in enumerate(blocks):
        if '|' in block: s_p.append([ (i, block) for block in block.split('|') ])
        else: s_q.append((i, block))

    # find cartesian product
    if s_p:

        # calculate product
        nested = reduce(lambda x,y:itertools.product(x,y), s_p)

        # flatten products
        product = map(list, [ nest if isinstance(nest, basestring)
                              else flatten(nest)
                              for nest in nested ])

        # pair products with categories
        try:
            permutation = []
            for pairable in product:
                stack = sorted(s_q + [tuple(pairable)]) # restore order
                permutation.append([categories, '(%s)' % ')('.join(map(lambda x:x[1], stack))])
        except:
            debug('w', '[GENERATOR] failed to pair categories and definitions\n')
            permutation = []

    # there is no product
    else: permutation = [[categories, definition]]
    return permutation

# HMDStruct
# ---------
#
# : An extensible basic unit of Hierarcical Multiple Dictionary.
#
class HMDStruct(object):
    '''
    + parameters:
    - {str} categories -- tab-delimited HMD categories.
    - {str} definition -- tab-delimited HMD definition.
    '''

    __slots__ = ['categories', 'definition']

    def __init__(self,
                 categories=None,
                 definition=''):
        self.categories = categories
        self.definition = definition

    def define(self, text):
        if not text: return

        # if `text` is a variable, define it as a `definition` since there would
        # be no `categories` to attribute with. The current variable format is:
        #
        # $variable = definition
        #
        # which makes '$' and '=' tokens "identifiers" to identify a variable.
        elif '$' in text and '=' in text:
            self.categories = None
            self.definition = text

        # otherwise, split the `text` using tab delimitor and define this schema
        # with `categories` and `definitions`. The current specification is:
        #
        # +-----------+--------------+-------------+-----------------+
        # | top-level | second-level | third-level |    |            |
        # | category  | category     | category    | .. | definition |
        # +-----------+--------------+-------------+-----------------+
        else:
            tokens = text.split('\t')
            if len(tokens) >= 2:
                self.categories,
                self.definition = [
                    tokens[:-1],
                    tokens[-1]]
        return bool(self.definition)

# HMDGenerator
# ------------
#
# : Generator logic customized for MindsLab.
#
class HMDGenerator(AbstractGenerator):
    '''
    + parameters:
    - {dict} syntax -- linguistic context.
    - {bool} hmd_optimized -- optimize the returned result.
    - {bool} hmd_sorted -- sort the returned result.
    - {bool} hmd_unique -- distinct returned result.
    - {int} max_categories -- allowed number of categories until the surplus
                              categories is merged with the bottom-most level
                              category.

    + notes:
    - In order to change the language context of the generator, define a new
      language syntax (e.g. "HMDSyntaxKorean") and pass the new dictionary
      instead of the "HMDSyntaxDefault" (English).
    '''

    def __init__(self,
                 syntax=HMDSyntaxDefault,
                 hmd_optimized=False,
                 hmd_sorted=False,
                 hmd_unique=False,
                 max_categories=3):

        # static
        self.grammar = HMDGrammar()
        self.syntax = syntax

        # initialization
        self.lexer = AbstractLexer(self.syntax)
        self.parser = AbstractParser(self.grammar)

        # build options
        self.hmd_optimized = hmd_optimized
        self.hmd_sorted = hmd_sorted
        self.hmd_unique = hmd_unique
        self.max_categories = max_categories

        # temporary states
        self.hmd = []

    # generate
    # --------
    #
    # : Generate a matrix-form of Hierarchical Multiple Dictionary from
    #   input text.
    #
    def generate(self, lines=[]):
        '''
        + parameters:
        - {list} lines -- input text split by newlines, tabs, or other
                          delimieter.
        '''
        if not lines: return ''

        # pre-process the input lines with generation flags (e.g. sort)
        # for the lines that exist (a.k.a. non-empty).
        try:
            self.hmd = [ str(line).strip() for line in lines if line ]
            if self.hmd_unique: self.hmd = list(set(self.hmd))
            if self.hmd_sorted: self.hmd.sort() # inline sorting
        except:
            debug('w', 'GENERATOR => unable to initialize hmd\n')
            raise

        # remove comments based on comment token from the `self.syntax`.
        # If all input were comments, return None since no generation is
        # necessary from this point.
        comment = r'^%s.+$' % self.syntax.get('COMMENT', '#')
        self.hmd = filter(lambda line:not re.findall(comment, line), self.hmd)
        if not self.hmd: return

        # convert each HMD lines into HMDStruct for easier manipulation.
        structs = []
        for hmd in self.hmd:
            struct = HMDStruct()
            if not struct.define(hmd):
                debug('w', "GENERATOR => cannot create schema from '%s'\n" % hmd)
            else:
                structs.append(struct)

        # create index of all categories and definitions in order to separately
        # syntax check the definitions before merging the two and generating
        # its matrix-form.
        categories = [
            struct.categories
            for struct in structs
            if struct.categories
        ]
        definitions = [
            struct.definition
            for struct in structs
            if struct.definition
        ]

        # tokenize and parse the definitions.
        tokens = self.lexer.lex(definitions)
        parsed = self.parser.parse(tokens) # syntax check occurs here.

        # merge the categories and the definitions to generate its matrix-form.
        return self.__build_matrix(categories, parsed)

    # __build_matrix
    # --------------
    #
    # build matrix from hmd data.
    #
    def __build_matrix(self, categories=[], definitions=[]):
        '''
        + categories {list} -- a list of categories.
        + definitions {list} -- a list of definitions.
        '''
        try: assert bool(categories) and len(categories) == len(definitions)
        except AssertionError:
            debug('w', '[GENERATOR] merging not possible:\n')
            debug('d', 'categories   -> %i\n' % len(categories))
            debug('d', 'definition -> %i\n' % len(definitions))
            sys.exit(1)

        # standardize categories count
        matrix = []
        limit = min(min(map(len, categories)), self.max_categories) # find the smallest
        for i in xrange(len(categories)):

            # struct
            categories, definition = categories[i], definitions[i]

            # normalize categories count
            deviation = int(len(categories) - limit)
            distance = 0 - deviation # distance from origin
            if deviation >= 0: categories.extend([''] * distance)
            else:
                partition = abs(distance - 1)
                categories = categories[partition:].append("_".join(categories[:partition]))

            # compile matrix
            for permutation in permute(categories, definition):
                if not permutation: pass
                categories, definition = permutation
                matrix.append('\t'.join([
                    '\t'.join(categories), # categories
                    '$'.join(definition[1:-1].split(')(')) # definition
                ]))

        return '\n'.join(set(matrix))
