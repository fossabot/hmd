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

'''
SOURCE HEADER:

[class]
i.  HMDStruct
ii. HMDGenerator
'''

# i. HMDStruct
# ------------
#
# : An extensible basic unit of Hierarcical Multiple Dictionary.
#
# [parameters]
#   - {str} categories -- tab-delimited HMD categories.
#   - {str} definition -- tab-delimited HMD definition.
#
class HMDStruct(object):

    __slots__ = ['categories', 'definition']

    def __init__(self,
                 categories=None,
                 definition=''):
        self.categories = categories
        self.definition = definition

    def define(self, text):
        if not text: return

        # if `text` is a variable, define it as a `definition` since there would
        # be no `categories` to attribute this schema with.
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

# ii. HMDGenerator
# ----------------
#
# : Generator logic customized for MindsLab.
#
# [parameters]
#   - {int} max_categories -- allowed number of categories until the surplus
#           categories is merged with the bottom-most level category.
#   - {bool} hmd_optimized -- optimization.
#   - {bool} hmd_sorted -- sort the output result.
#   - {bool} hmd_unique -- distinct output result.
#   - {dict} syntax -- linguistic syntax.
#
# [notes]
#   1. In order to change the language context of the generator, define a new
#      language syntax (e.g. "HMDSyntaxKorean") and pass the new dictionary
#      instead of the "HMDSyntaxDefault" (English).
#
class HMDGenerator(AbstractGenerator):

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
        self.matrix = None
        self.hmd = None

    #
    # public
    #

    def generate(self, lines=[]):
        ''' compile hmd dictionary to matrix form.
        '''
        if not lines: return
        self.__initialize_hmd(lines)

        # delete comments
        self.__remove_comments()
        if not self.hmd: return

        # divide lines into hmd-schema
        schemas = []
        for hmd in self.hmd:
            schema = HMDStruct()
            if not schema.define(hmd):
                debug('w', "[GENERATOR] cannot create schema: '%s'\n" % hmd)
                pass # disregard the unpackable format and continue
            else: schemas.append(schema)

        # categories must be length-filtered due to variables
        categories = [ schema.categories for schema in schemas if schema.categories ]
        definitions = [ schema.definition for schema in schemas ]

        # parse and generate matrix
        tokens = self.lexer.lex(definitions)
        definitions = self.parser.parse(tokens)
        return self.__build_matrix(categories, definitions)

    #
    # private
    #

    def __initialize_hmd(self, lines=[]):
        ''' initialize self.hmd with raw lines.
        + lines {list} -- lines to convert from hmd to matrix.
        '''
        try:
            self.hmd = [ line.strip() for line in lines if line ]
            if self.hmd_unique: self.hmd = list(set(self.hmd)) # unique
            if self.hmd_sorted: self.hmd.sort() # sort
        except:
            debug('w', '[GENERATOR] unable to initialize hmd\n')
            sys.exit(1)

    def __remove_comments(self):
        ''' remove all commented lines.
        '''
        if not self.hmd: return
        comments = r'^%s.+$' % self.syntax.get('COMMENT', '#')
        self.hmd = filter(lambda x:not re.findall(comments, x), self.hmd)

    def __flatten(self, L=[]):
        ''' recursively flatten nested lists/tuples.
        + L {list|tuple} -- nested list/tuple.
        '''
        if not L: return L
        if isinstance(L[0], tuple) or isinstance(L[0], list):
            return self.__flatten(L[0]) + self.__flatten(L[1:])
        return L[:1] + self.__flatten(L[1:])

    def __permute(self, categories=[], definition=''):
        ''' get cartesian product of definitions and pair with categories.
        + categories {list} -- a list of categories.
        + definition {list} -- definition.
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
                                  else self.__flatten(nest)
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

    def __build_matrix(self, categories=[], definitions=[]):
        ''' build matrix from hmd data.
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

            # schema
            categories, definition = categories[i], definitions[i]

            # normalize categories count
            deviation = int(len(categories) - limit)
            distance = 0 - deviation # distance from origin
            if deviation >= 0: categories.extend([''] * distance)
            else:
                partition = abs(distance - 1)
                categories = categories[partition:].append("_".join(categories[:partition]))

            # compile matrix
            for permutation in self.__permute(categories, definition):
                if not permutation: pass
                categories, definition = permutation
                matrix.append('\t'.join([
                    '\t'.join(categories), # categories
                    '$'.join(definition[1:-1].split(')(')) # definition
                ]))

        return '\n'.join(set(matrix))
