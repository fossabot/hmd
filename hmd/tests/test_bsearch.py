#!/usr/bin/env python

from src.abstract.matcher.bsearch import bSearchMatcher
from src.abstract.matcher.bsearch import bSearchPreprocessor

import unittest

class TestbSearch(unittest.TestCase):
    '''
    : unit tests for automata class.
    '''

    bp = bSearchPreprocessor()
    bm = bSearchMatcher()

    #
    # pre-processor
    #

    def test_bsearch_preprocessor_type(self):
        self.assertTrue(isinstance(self.bp, bSearchPreprocessor))

    def test_bsearch_preprocessor_clean_normal_alpha(self):
        text = 'a bc def ghij klmno pqrstu vwxy z'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text),
                          text)

    def test_bsearch_preprocessor_clean_normal_alphanumeric(self):
        text = 'a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text),
                          text)

    def test_bsearch_preprocessor_clean_trim_alphanumeric(self):
        text = ' a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90 '
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text),
                          text.strip())

    def test_bsearch_preprocessor_clean_ltrim_alphanumeric(self):
        text = ' a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90'
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text),
                          text.lstrip())

    def test_bsearch_preprocessor_clean_rtrim_alphanumeric(self):
        text = 'a bc def ghij klmno pqrstu vwxy z 1234 5 6 z7 a8 90 '
        self.assertEquals(self.bp._bSearchPreprocessor__clean(text),
                          text.rstrip())

    #
    # matcher
    #

    def test_bsearch_match_type(self):
        self.assertTrue(isinstance(self.bm, bSearchMatcher))
