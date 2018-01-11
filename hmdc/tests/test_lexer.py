#!/usr/bin/env python

from src.abstract.lexer.lexer import AbstractLexer
from src.abstract.lexer.token import AbstractToken

import unittest

class TestLexer(unittest.TestCase):
    '''
    : unit tests for lexer class.
    '''

    lexer = AbstractLexer()

    def test_lexer_string_blank(self):
        attempt = self.lexer.lex('')
        answer = []
        self.assertEqual(attempt, answer)

    #
    # strings
    #

    def test_lexer_string_short_A(self):
        attempt = str(self.lexer.lex('A'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'A'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_short_a(self):
        attempt = str(self.lexer.lex('a'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'a'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_short_Z(self):
        attempt = str(self.lexer.lex('Z'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'Z'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_short_z(self):
        attempt = str(self.lexer.lex('z'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'z'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_long_A(self):
        attempt = str(self.lexer.lex('AA'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'A'},
        	      {'y': 0, 'x': 1, 'type': 'STRING', 'value': 'A'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_long_a(self):
        attempt = str(self.lexer.lex('aa'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'a'},
        	      {'y': 0, 'x': 1, 'type': 'STRING', 'value': 'a'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_long_Z(self):
        attempt = str(self.lexer.lex('ZZ'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'Z'},
                      {'y': 0, 'x': 1, 'type': 'STRING', 'value': 'Z'}])
        self.assertEqual(attempt, answer)

    def test_lexer_string_long_z(self):
        attempt = str(self.lexer.lex('zz'))
        answer = str([{'y': 0, 'x': 0, 'type': 'STRING', 'value': 'z'},
                      {'y': 0, 'x': 1, 'type': 'STRING', 'value': 'z'}])
        self.assertEqual(attempt, answer)

    #
    # numbers
    #

    def test_lexer_number_one(self):
        attempt = str(self.lexer.lex('1'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '1'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_two(self):
        attempt = str(self.lexer.lex('2'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '2'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_three(self):
        attempt = str(self.lexer.lex('3'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '3'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_four(self):
        attempt = str(self.lexer.lex('4'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '4'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_five(self):
        attempt = str(self.lexer.lex('5'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '5'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_six(self):
        attempt = str(self.lexer.lex('6'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '6'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_seven(self):
        attempt = str(self.lexer.lex('7'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '7'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_eight(self):
        attempt = str(self.lexer.lex('8'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '8'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_nine(self):
        attempt = str(self.lexer.lex('9'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '9'}])
        self.assertEqual(attempt, answer)

    def test_lexer_number_zero(self):
        attempt = str(self.lexer.lex('0'))
        answer = str([{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '0'}])
        self.assertEqual(attempt, answer)

    #
    # symbols
    #

    def test_lexer_symbol_random_01(self):
        attempt = str(self.lexer.lex('@'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '@'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_02(self):
        attempt = str(self.lexer.lex('+'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '+'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_03(self):
        attempt = str(self.lexer.lex('!'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '!'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_04(self):
        attempt = str(self.lexer.lex('#'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '#'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_05(self):
        attempt = str(self.lexer.lex('{'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '{'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_06(self):
        attempt = str(self.lexer.lex('}'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '}'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_07(self):
        attempt = str(self.lexer.lex('-'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '-'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_08(self):
        attempt = str(self.lexer.lex('_'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '_'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_09(self):
        attempt = str(self.lexer.lex('^'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '^'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_10(self):
        attempt = str(self.lexer.lex('%'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '%'}])
        self.assertEqual(attempt, answer)

    def test_lexer_symbol_random_11(self):
        attempt = str(self.lexer.lex('.'))
        answer = str([{'y': 0, 'x': 0, 'type': 'SYMBOL', 'value': '.'}])
        self.assertEqual(attempt, answer)

    #
    # space
    #

    def test_lexer_space_single(self):
        attempt = str(self.lexer.lex(' '))
        answer = str([{'y': 0, 'x': 0, 'type': 'SPACE', 'value': ' '}])
        self.assertEqual(attempt, answer)

    def test_lexer_space_multiple(self):
        attempt = str(self.lexer.lex('   '))
        answer = str([{'y': 0, 'x': 0, 'type': 'SPACE', 'value': ' '},
                      {'y': 0, 'x': 1, 'type': 'SPACE', 'value': ' '},
                      {'y': 0, 'x': 2, 'type': 'SPACE', 'value': ' '}])
        self.assertEqual(attempt, answer)

    #
    # mixed
    #

    def test_lexer_mixed_index_type_same(self):
        attempt = str(self.lexer.lex(['0',1,23,456,7890]))
        answer = str([[{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '0'}],
                      [{'y': 1, 'x': 0, 'type': 'NUMBER', 'value': '1'}],
                      [{'y': 2, 'x': 0, 'type': 'NUMBER', 'value': '2'},
                       {'y': 2, 'x': 1, 'type': 'NUMBER', 'value': '3'}],
                      [{'y': 3, 'x': 0, 'type': 'NUMBER', 'value': '4'},
                       {'y': 3, 'x': 1, 'type': 'NUMBER', 'value': '5'},
                       {'y': 3, 'x': 2, 'type': 'NUMBER', 'value': '6'}],
                      [{'y': 4, 'x': 0, 'type': 'NUMBER', 'value': '7'},
                       {'y': 4, 'x': 1, 'type': 'NUMBER', 'value': '8'},
                       {'y': 4, 'x': 2, 'type': 'NUMBER', 'value': '9'},
                       {'y': 4, 'x': 3, 'type': 'NUMBER', 'value': '0'}]])
        self.assertEqual(attempt, answer)

    def test_lexer_mixed_index_type_different(self):
        attempt = str(self.lexer.lex(['0','A','bc','$%^',7890]))
        answer = str([[{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '0'}],
                      [{'y': 1, 'x': 0, 'type': 'STRING', 'value': 'A'}],
                      [{'y': 2, 'x': 0, 'type': 'STRING', 'value': 'b'},
                       {'y': 2, 'x': 1, 'type': 'STRING', 'value': 'c'}],
                      [{'y': 3, 'x': 0, 'type': 'SYMBOL', 'value': '$'},
                       {'y': 3, 'x': 1, 'type': 'SYMBOL', 'value': '%'},
                       {'y': 3, 'x': 2, 'type': 'SYMBOL', 'value': '^'}],
                      [{'y': 4, 'x': 0, 'type': 'NUMBER', 'value': '7'},
                       {'y': 4, 'x': 1, 'type': 'NUMBER', 'value': '8'},
                       {'y': 4, 'x': 2, 'type': 'NUMBER', 'value': '9'},
                       {'y': 4, 'x': 3, 'type': 'NUMBER', 'value': '0'}]])
        self.assertEqual(attempt, answer)

    def test_lexer_mixed_index_type_empty(self):
        attempt = str(self.lexer.lex(['0','A','bc','$%^','','']))
        answer = str([[{'y': 0, 'x': 0, 'type': 'NUMBER', 'value': '0'}],
                      [{'y': 1, 'x': 0, 'type': 'STRING', 'value': 'A'}],
                      [{'y': 2, 'x': 0, 'type': 'STRING', 'value': 'b'},
                       {'y': 2, 'x': 1, 'type': 'STRING', 'value': 'c'}],
                      [{'y': 3, 'x': 0, 'type': 'SYMBOL', 'value': '$'},
                       {'y': 3, 'x': 1, 'type': 'SYMBOL', 'value': '%'},
                       {'y': 3, 'x': 2, 'type': 'SYMBOL', 'value': '^'}],
                      [],
                      []])
        self.assertEqual(attempt, answer)
