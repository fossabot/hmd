#!/usr/bin/env python

from src.abstract.lexer.token import AbstractToken
from src.debug import *

from os import path
from re import match
import errno
import sys

class AbstractLexer(object):
    ''' an abstract lexicographic analyzer that tokenizes a text using input grammar (regex).
    params:
      + rules {dict} -- custom dictionary of regex to lexical analyze.
    '''

    def __init__(self, rules={}):
        self.rules = rules or { # default
            'SYMBOL': r'[^A-Za-z\d\s]+',
            'STRING': r'[A-Za-z]+',
            'NUMBER': r'[\d]+',
            'SPACE': r'[ ]+'
        }

    #
    # public
    #

    def lex(self, tokenable):
        ''' prototype to lex a string or enumerable strings (e.g. list or tuple).
        + tokenable {str|list|tuple} -- input string(s) to tokenize.
        '''
        if not (isinstance(tokenable, basestring) or \
                isinstance(tokenable, tuple) or \
                isinstance(tokenable, list)):
            debug('w', "lex only possible with string/tuple/list: received => '%s'" % (type(tokenable)))
            return []

        # string
        if isinstance(tokenable, basestring):
            return [ AbstractToken(value=tokenable[i],
                                   type=self.__tokenize(tokenable[i]),
                                   x=i, y=0)
                     for i in xrange(len(tokenable)) ]

        # tuple/list
        else:
            tokenable = map(str, tokenable) # convert
            return [ [ AbstractToken(value=tokenable[i][j],
                                     type=self.__tokenize(tokenable[i][j]),
                                     x=j, y=i)
                       for j in xrange(len(tokenable[i])) ]
                     for i in xrange(len(tokenable)) ]

    #
    # private
    #

    def __tokenize(self, character=''):
        ''' prototype to tokenize a character.
         + charcter {str} -- a character to be tokenized.
        '''
        if not isinstance(character, str) or 1 != len(character):
            debug('w', "can't be tokenized: '%s'" % str(character))
            return None
        for rule in sorted(self.rules.values()):
            token = (self.rules.keys()[self.rules.values().index(rule)]
                     if match(rule, character) else None)
            if token: break
        return token
