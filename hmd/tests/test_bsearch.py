#!/usr/bin/env python

from src.abstract.matcher.bsearch import bSearchMatcher
from src.abstract.matcher.bsearch import bSearchPreprocessor

import unittest

class TestbSearch(unittest.TestCase):
    '''
    : unit tests for b-search algorithm.
    '''

    bp = bSearchPreprocessor()
    bm = bSearchMatcher()

    #
    # pre-processor
    #

    def test_bsearch_preprocessor_inherited_type(self):
        self.assertTrue(isinstance(self.bp, bSearchPreprocessor))

    def test_bsearch_preprocessor_clean_normal_alpha(self):
        text = 'a bc def ghij klmno pqrstu vwxy z'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text), text)

    def test_bsearch_preprocessor_clean_normal_alphanumeric(self):
        text = 'a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text), text)

    def test_bsearch_preprocessor_clean_trim_alphanumeric(self):
        text = ' a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90 '
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text), text.strip())

    def test_bsearch_preprocessor_clean_ltrim_alphanumeric(self):
        text = ' a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text), text.lstrip())

    def test_bsearch_preprocessor_clean_rtrim_alphanumeric(self):
        text = 'a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90 '
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text), text.rstrip())

    def test_bsearch_preprocessor_clean_dirty_1(self):
        attempt = 'a#b$0~1 '
        answer = 'a b 0 1'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(attempt), answer)

    def test_bsearch_preprocessor_clean_dirty_2(self):
        attempt = '     aaa#bbbbb$0~1 2+   '
        answer = 'aaa bbbbb 0 1 2'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(attempt), answer)

    def test_bsearch_preprocessor_clean_dirty_3(self):
        attempt = '~!@#$%^&*()_+'
        answer = ''
        self.assertEquals(self.bp._bSearchPreprocessor__clean(attempt), answer)

    def test_bsearch_preprocessor_clean_dirty_4(self):
        attempt = '~!@#$%^&*()_+1a'
        answer = '1a'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(attempt), answer)

    #
    # matcher
    #

    def test_bsearch_match_inherited_type(self):
        self.assertTrue(isinstance(self.bm, bSearchMatcher))
