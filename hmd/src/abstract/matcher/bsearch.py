#!/usr/bin/env python

class bSearchPreprocessor(object):
    ''' custom b-search algorithm pre-processor.
    '''

    __slots__ = ['valid_text']

    def __init__(self):
        import re # lazy load
        self.valid_text = re.compile('[^\W_]+')

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
    ''' custom b-search algorithm matcher.
    '''

    def __init__(self,
                 bucket=[],
                 basket=[]):
        # lazy load
        import ast
        import re
        self.valid_text = re.compile('[^\W_]+')
        self.bucket = bucket
        self.basket = basket

    #
    # public
    #

    def get_bucket(self):
        return self.bucket

    def get_basket(self):
        return self.basket

    def load_bucket(self, bucket):
        if bucket and isinstance(bucket, list):
            self.bucket = bucket
        return self.bucket == bucket

    def load_basket(self, basket):
        if basket and isinstance(basket, list):
            self.basket = basket
        return self.basket == basket

    def match(self, search_terms=[]):
        if not search_terms: return

        # check for optimized search
        if all(map(lambda x:self.valid_text.match(x), search_terms)):
            return self.__optimized_basic_match(search_terms)

        # non-optimized search
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
        try: _ = [ self.bucket.get(term.__len__()).values()
                   for term in search_terms ]
        except AttributeError: return
        return all([ term in _[i]
                     if not set(_[i]).intersection(set(self.basket))
                     else False
                     for i, term in enumerate(search_terms) ])
