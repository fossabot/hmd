#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomata, AbstractAutomataMachine
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

class HMDSchema(object):
    ''' an abstract hmd schema.
    '''

    def __init__(self):
        self.category = None
        self.definition = None

    def view(self):
        ''' view schema.
        '''
        return (self.category,
                self.definition)

    def pack(self, line=''):
        ''' pack line into schema.
        '''
        if not line: return
        if all([ x in line for x in ('$', '=') ]):
            self.definition = line
        else:
            tokens = line.split('\t')
            if len(tokens) < 2: return
            self.category, self.definition = [
                tokens[:-1],
                tokens[-1]]
        return True

    def unpack(self):
        ''' unpack schema into line.
        '''
        try: line = '\t'.join(self.category, self.definition)
        except:
            debug('w', 'incorrect schema structure => defaulting to empty schema.\n')
            line = ''
        return line

class HMDGenerator(AbstractGenerator):
    ''' default hierarchial multiple dictionary generator.
    '''

    def __init__(self,
                 max_categories=10,
                 hmd_optimized=False,
                 hmd_sorted=False,
                 hmd_unique=False):

        # static
        self.syntax = HMDSyntaxDefault
        self.grammar = HMDGrammar()

        # initialization
        self.lexer = AbstractLexer(self.syntax)
        self.parser = AbstractParser(self.grammar)

        # build options
        self.max_categories = max_categories
        self.hmd_optimized = hmd_optimized
        self.hmd_sorted = hmd_sorted
        self.hmd_unique = hmd_unique

        # temporary states
        self.hmd = None
        self.matrix = None

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
            schema = HMDSchema()
            if not schema.pack(hmd):
                debug('w', "GENERATOR: cannot create schema: '%s'.\n" % hmd)
                pass # disregard the unpackable format and continue
            else: schemas.append(schema)

        # categories must be length-filtered due to variables
        categories = [ schema.category for schema in schemas if schema.category ]
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
            debug('w', 'GENERATOR: unable to initialize hmd.\n')
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

    def __permute(self, category=[], definition=''):
        ''' get cartesian product of definitions and pair with category.
        + category {list} -- a list of category.
        + definition {list} -- definition.
        '''
        try: blocks = definition[1:-1].split(')(')
        except IndexError: blocks = []
        if not blocks: return blocks

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
                    permutation.append([category, '(%s)' % ')('.join(map(lambda x:x[1], stack))])
            except:
                debug('w', 'GENERATOR: failed to pair categories and definitions.\n')
                permutation = []

        # there is no product
        else: permutation = [[category, definition]]
        return permutation

    def __build_matrix(self, categories=[], definitions=[]):
        ''' build matrix from hmd data.
        + categories {list} -- a list of categories.
        + definitions {list} -- a list of definitions.
        '''
        try: assert bool(categories) and len(categories) == len(definitions)
        except AssertionError:
            debug('w', 'GENERATOR: merging not possible:\n')
            debug('d', 'category   -> %i\n' % len(categories))
            debug('d', 'definition -> %i\n' % len(definitions))
            sys.exit(1)

        # standardize category count
        matrix = []
        limit = min(min(map(len, categories)), self.max_categories) # find the smallest
        for i in xrange(len(categories)):

            # schema
            category, definition = categories[i], definitions[i]

            # normalize category count
            deviation = int(len(category) - limit)
            distance = 0 - deviation # distance from origin
            if deviation >= 0: category.extend([''] * distance)
            else:
                partition = abs(distance - 1)
                category = category[partition:].append("_".join(category[:partition]))

            # compile matrix
            for permutation in self.__permute(category, definition):
                if not permutation: pass
                category, definition = permutation
                matrix.append('\t'.join([
                    '\t'.join(category), # category
                    '$'.join(definition[1:-1].split(')(')) # definition
                ]))

        return '\n'.join(set(matrix))
