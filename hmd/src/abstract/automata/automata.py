#!/usr/bin/env python

class AbstractAutomata(object):
    ''' an abstract automata that stores state, transition(s), start and end state.
    params:
      + state {str} -- a state
      + transition {list} -- transition from a state to another state
      + basetype {str} -- first-generation primitive type
      + start {bool} -- initial/starting state (q_0)
      + final {bool} -- final/accepting state (q_f)
    '''
    def __init__(self,
                 state='',
                 transition=[],
                 basetype='',
                 start=False,
                 final=False):
        self.state = state
        self.transition = transition
        self.basetype = basetype
        self.start = start
        self.final = final

class AbstractAutomataMachine(object):
    ''' an abstract machine that stores automata.
    '''

    def __init__(self):
        self.cache = []

    def __len__(self):
        return self.cache.__len__()

    #
    # public
    #

    def get_state(self, state):
        ''' get a state.
        '''
        return [ automata.state
                 for automata in self.cache
                 if automata.state == state ]

    def get_states(self):
        ''' get the state of all automata.
        '''
        return [ automata.state
                 for automata in self.cache ]

    def get_transition(self, state):
        ''' get defined transition(s) for a state in grammar.
        params:
          + state {AbstractAutomata} -- a particular automata
        '''
        automata = filter(lambda x:x.state == state, self.cache)
        return (map(lambda x:x.transition, automata)[0]
                if bool(automata) else [])

    def get_transitions(self):
        ''' get all possible transitions of automata.
        '''
        return [ automata.transition
                 for automata in self.cache ]

    def add_state(self, automata):
        ''' add automata state.
        params:
          + automata {AbstractAutomata} -- an automata
        '''
        if isinstance(automata, AbstractAutomata):
            self.cache.append(automata)
