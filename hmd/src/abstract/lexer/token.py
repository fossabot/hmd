#!/usr/bin/env python

class AbstractToken(object):
    ''' an abstract token.
    '''

    def __init__(self,
                 value=None,
                 type=None,
                 x=-1,
                 y=-1):
        '''
        params:
          + value {str} -- tokenized value.
          + type {str} -- token type.
          + x {int} -- x-coordinate of value.
          + y {int} -- y-coordinate of value.
        '''
        self.type = type
        self.value = value
        self.x = x
        self.y = y

    def __repr__(self):
        return {
            'value': self.value,
            'type': self.type,
            'x': self.x,
            'y': self.y
        }.__str__()

    #
    # public
    #

    def keys(self):
        ''' prototype to get all keys.
        '''
        return tuple(self.__dict__.keys())

    def values(self):
        ''' prototype to get all values.
        '''
        return tuple(self.__dict__.values())

    def exists(self, key):
        ''' prototype to check if a key exists.
        params:
          + key {str} -- key to check.
        '''
        return self.__dict__.__contains__(key)

    def get(self, key):
        ''' prototype to get value of a given key.
        params:
          + key {str} -- key to get value.
        '''
        return (self.__dict__[key] if self.exists(key) else None)

    def set(self, key, value):
        ''' prototype to set value of a key.
        params:
          + key {str} -- key to replace value with.
          + value {str} -- value to replace with.
        '''
        self.__dict__[key] = (value if key else None)
        return self.__dict__.get(key)

    def delete(self, key):
        ''' prototype to delete a key.
        params:
          + key {str} -- key to delete.
        '''
        if self.exists(key):
            self.__dict__.pop(key)
        return not self.exists(key)
