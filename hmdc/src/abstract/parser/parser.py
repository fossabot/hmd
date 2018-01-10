#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomataMachine
from src.abstract.lexer.token import AbstractToken
from src.debug import *

from collections import deque
import re
import sys

class AbstractParser(object):
    ''' an abstract parser to convert tokens into build instruction code.
    params:
      + grammar {AbstractAutomataMachine} -- grammar to check and parse tokens.
    '''

    def __init__(self, grammar):

        # grammar
        self.grammar = grammar.get_automata()
        self.variables = {}

        # syntax
        # - "stack" used to check syntax.
        # - "heap" used to store parsed block of code.
        self.syntax_stack = deque([None, None], maxlen=2) # circular queue
        self.syntax_heap = []

        # parsed result
        self.code = []

    #
    # public
    #

    def parse(self, tokens=[]):
        ''' prototype to parse lexed single line string or a list of strings.
        params:
          + tokens {list|list[list]} -- list or nested lists of tokens from lexer.
        '''
        if not tokens: return []
        if not all([isinstance(token, list) for token in tokens]):
            self.__evaluate(tokens) # tokens
        else: [ self.__evaluate(token) for token in tokens ] # nested tokens
        return self.code

    #
    # private
    #

    def __evaluate(self, tokens=[]):
        ''' prototype to parse single line of tokens.
        params:
          + tokens {list} -- list of tokens from lexer.
        '''
        if len(tokens) < 2 or not all(map(lambda token:isinstance(token, AbstractToken), tokens)):
            debug('w', 'PARSER: not enough tokens or not abstract tokens.\n')
            self.__reset_stack()
            return

        try: line = ''.join([ token.value for token in tokens ])
        except:
            debug('b', 'PARSER: invalid value type in tokens.\n')
            self.__reset_stack()
            return

        if '$' in line:

            # find all unique identifiers
            identifiers = set(re.findall(r'\$[A-Za-z]{1}\w*', line))

            # store/interpolate identifiers
            for v_i in identifiers:
                if '=' in line:
                    definition = re.findall(r'=\s*.+$', line) # extract definition
                    v_di = re.sub(r'^=\s*', '', definition[0]) # ltrim and rtrim
                    try: v_d = tokens[line.index(v_di):line.index('#')] # upto comment
                    except ValueError: v_d = tokens[line.index(v_di):] # upto EOL
                    self.variables[v_i] = v_d
                else:
                    if v_i in self.variables.keys():
                        stack = re.findall('\%s' % v_i, line)
                        for pop in stack:
                            i = line.index(v_i)
                            tokens = tokens[:i] + self.variables[v_i] + tokens[i+len(v_i):]
                            line = ''.join([ token.value for token in tokens ]) # update
                        if '$' not in line: self.__parse_tokens(tokens)
                    else:
                        debug('w', "variable '%s' is not defined.\n" % v_i)
                        self.__reset_stack()

        # parse definition
        elif tokens[0].type == 'RULE_BEGIN' and tokens[-1].type == 'RULE_END':
            try: self.__parse_tokens(tokens)
            except:
                self.syntax_stack.append(tokens[0]) # debug
                self.syntax_stack.append(tokens[-1]) # debug
                self.__throw_syntax_error()

        else:
            self.syntax_stack.append(tokens[0]) # debug
            self.syntax_stack.append(tokens[-1]) # debug
            self.__throw_syntax_error()

    def __parse_tokens(self, tokens=[]):
        ''' prototype to parse tokens and add to code instruction.
        params:
          + tokens {list} -- list of tokens from lexer.
        '''
        self.syntax_stack.append(tokens[0])
        self.syntax_heap.append(tokens[0].value)
        for token in tokens[1::]:

            # check syntax
            self.syntax_stack.append(token)
            if not self.__is_valid_syntax():
                self.__throw_syntax_error()
                return

            # consolidate
            self.syntax_heap.append(token.value)

        # add instruction
        self.code.append(''.join(self.syntax_heap[:]))
        self.syntax_heap[:] = [] # clear

    def __is_valid_syntax(self):
        ''' prototype to syntax check.
        '''
        q_s, q_e = self.syntax_stack[0], self.syntax_stack[1] # queue start and end
        if not (q_s or q_e):
            return False

        # check valid transition
        try: return q_e.type in self.grammar.get_transition(q_s.type)
        except: return False

    def __throw_syntax_error(self):
        ''' print syntax error message.
        '''
        debug('w', 'SYNTAX: incorrect transition:\n')
        self.__print_stack()
        self.__reset_stack()

    #
    # debug
    #

    def __print_stack(self):
        sys.stdout.write("=> curret: %s\n" % (self.syntax_stack[0] or {}) +\
                         "=> next:   %s\n" % (self.syntax_stack[1] or {}))

    def __reset_stack(self):
        self.syntax_stack.clear()
        self.syntax_heap = []
        self.code = None
