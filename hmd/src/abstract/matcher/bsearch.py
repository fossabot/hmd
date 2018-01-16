#!/usr/bin/env python

class bSearchPreprocessor(object):
    ''' an bucket-search algorithm pre-processor implementation.
    '''

    __slots__ = ['valid_text']

    def __init__(self):
        import re # lazy load
        self.valid_text = re.compile('[A-Za-z0-9]+')

    #
    # public
    #

    def parse(self, texts):
        if isinstance(texts, basestring):
            return self.__process(texts)
        elif isinstance(texts, list) or \
             isinstance(texts, tuple):
            return [ self.__process(str(text))
                     for text in texts ]

    #
    # private
    #

    def __process(self, text):
        _ = self.__clean(text or '')
        bucket, terms = {}, _.split()
        try:
            for i, term in enumerate(terms):
                size = term.__len__()
                if bucket.get(size): bucket[size][i] = term
                else: bucket[size] = {i: term}
        except: pass
        return bucket

    def __clean(self, text):
        # TODO: cover more encoding types.
        try: _ = (text or '').strip().encode('UTF-8').lower()
        except UnicodeDecodeError: raise
        return ' '.join(self.valid_text.findall(_))

class bSearchMatcher(object):

    __slots__ = ['bucket']

    def __init__(self, bucket=[]):
        import ast # lazy load
        self.bucket = bucket

    #
    # public
    #

    def match(self, search_terms=[]):
        if not search_terms: return
        for term in search_terms:
            size = term.__len__()
            res = self.bucket.get(size)
            if not res: return
            _ = res.values()
            if not term in _: return
        return True

    #
    # private
    #

    def __optimized_basic_match(self, search_terms=[]):
        '''
        '''
        if not search_terms: return

        return
