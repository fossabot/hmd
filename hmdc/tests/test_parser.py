#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomataMachine
from src.abstract.lexer.lexer import AbstractLexer
from src.abstract.lexer.token import AbstractToken
from src.abstract.parser.parser import AbstractParser
from src.mindslab.grammar import HMDGrammar
from src.mindslab.syntax import *

import unittest

class TestParser(unittest.TestCase):
    '''
    : unit tests for parser class.
    '''

    lexer = AbstractLexer(HMDSyntaxDefault)
    parser = AbstractParser(HMDGrammar())

    def test_parser_empty_string(self):
        attempt = self.parser.parse('')
        answer = []
        self.assertEqual(attempt, answer)

    def test_parser_empty_list(self):
        attempt = self.parser.parse([])
        self.assertFalse(attempt)

    def test_parser_empty_list_string(self):
        attempt = self.parser.parse([''])
        self.assertFalse(attempt)

    def test_parser_empty_list_strings(self):
        attempt = self.parser.parse(['',''])
        self.assertFalse(attempt)

    #
    # syntax: valid
    #

    #
    # syntax: invalid
    #

    def test_parser_invalid_syntax_empty(self):
        hmd = '()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_leading_double(self):
        hmd = '(()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_trailing_double(self):
        hmd = '())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_nested(self):
        hmd = '(())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequel(self):
        hmd = '+'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequels(self):
        hmd = '++'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequel_missing_count(self):
        hmd = '(+)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequel_missing_count_nested(self):
        hmd = '(+())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequel_leading_missing_count(self):
        hmd = '+()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_sequel_trailing_missing_count(self):
        hmd = '()+'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequel(self):
        hmd = '-'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequels(self):
        hmd = '--'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequel_missing_count(self):
        hmd = '(-)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequel_missing_count_nested(self):
        hmd = '(-())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequel_leading_missing_count(self):
        hmd = '-()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_prequel_trailing_missing_count(self):
        hmd = '()-'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_following(self):
        hmd = '@'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_followings(self):
        hmd = '@@'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_following_missing_count(self):
        hmd = '(@)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_following_missing_count_nested(self):
        hmd = '(@())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_following_leading_missing_count(self):
        hmd = '@()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_following_trailing_missing_count(self):
        hmd = '()@'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not(self):
        hmd = '!'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_space_between(self):
        hmd = '! '
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_nots(self):
        hmd = '!!'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_nots_space_between(self):
        hmd = '! !'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_missing_count(self):
        hmd = '(!)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_missing_count_nested(self):
        hmd = '(!())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_leading_missing_count(self):
        hmd = '!()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_trailing_missing_count(self):
        hmd = '()!'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat(self):
        hmd = '^'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hats(self):
        hmd = '^^'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat_space_between(self):
        hmd = '^ 1'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat_missing_count(self):
        hmd = '(^)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat_missing_count_nested(self):
        hmd = '(^())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat_leading_missing_count(self):
        hmd = '^()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_hat_trailing_missing_count(self):
        hmd = '()^'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcard(self):
        hmd = '%'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcards(self):
        hmd = '%%'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcard_missing_count(self):
        hmd = '(%)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcard_missing_count_nested(self):
        hmd = '(%())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcard_leading_missing_count(self):
        hmd = '%()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_wildcard_trailing_missing_count(self):
        hmd = '()%'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_or(self):
        hmd = '|'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_ors(self):
        hmd = '||'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_or_missing_count(self):
        hmd = '(|)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_or_missing_count_nested(self):
        hmd = '(|())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_or_leading_missing_count(self):
        hmd = '|()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_or_trailing_missing_count(self):
        hmd = '()|'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifier(self):
        hmd = '$'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifiers(self):
        hmd = '$$'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifier_missing_count(self):
        hmd = '($)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifier_missing_count_nested(self):
        hmd = '($())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifier_leading_missing_count(self):
        hmd = '$()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_identifier_trailing_missing_count(self):
        hmd = '()$'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignment(self):
        hmd = '='
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignments(self):
        hmd = '=='
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_not_assignments(self):
        hmd = '!='
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignment_missing_count(self):
        hmd = '(=)'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignment_missing_count_nested(self):
        hmd = '(=())'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignment_leading_missing_count(self):
        hmd = '=()'
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)

    def test_parser_invalid_syntax_assignment_trailing_missing_count(self):
        hmd = '()='
        tokens = self.lexer.lex(hmd)
        attempt = self.parser.parse(tokens)
        self.assertFalse(attempt)
