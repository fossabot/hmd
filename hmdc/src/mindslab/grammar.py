#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomata,
from src.abstract.automata.automata import AbstractAutomataMachine

class HMDGrammar(object):
    ''' default hierarchial multiple dictionary grammar.
    '''

    def __init__(self):

        self.automata = AbstractAutomataMachine()

        # STRING
        self.automata.add_state(
            AbstractAutomata(
                state='STRING',
                basetype='LITERAL',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'RULE_END',
                    'GRAMMAR_OR',
                    'MATCH_BEFORE',
                    'VARIABLE_IDENTIFIER',
                    'VARIABLE_ASSIGNMENT'
                ]
            )
        )

        # NUMBER
        self.automata.add_state(
            AbstractAutomata(
                state='NUMBER',
                basetype='LITERAL',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'RULE_END',
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'VARIABLE_ASSIGNMENT',
                    'MATCH_ALWAYS',
                    'MATCH_NOT'
                ]
            )
        )

        # SPACE
        self.automata.add_state(
            AbstractAutomata(
                state='SPACE',
                basetype='LITERAL',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'RULE_END',
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'VARIABLE_ASSIGNMENT'
                ]
            )
        )

        # RULE_BEGIN
        self.automata.add_state(
            AbstractAutomata(
                state='RULE_BEGIN',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'MATCH_NEXT',
                    'MATCH_BEFORE',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'VARIABLE_IDENTIFIER'
                ]
            )
        )

        # RULE_END
        self.automata.add_state(
            AbstractAutomata(
                state='RULE_END',
                basetype='EXPRESSION',
                transition=[
                    'RULE_BEGIN',
                    'VARIABLE_IDENTIFIER'
                ]
            )
        )

        # MATCH_NEXT
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_NEXT',
                basetype='EXPRESSION',
                transition=[
                    'NUMBER'
                ]
            )
        )

        # MATCH_BEFORE
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_BEFORE',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER'
                ]
            )
        )

        # MATCH_ALWAYS
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_ALWAYS',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD'
                ]
            )
        )

        # MATCH_NOT
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_NOT',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'MATCH_BEFORE',
                    'MATCH_NEXT'
                ]
            )
        )

        # GRAMMAR_HAT
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR_HAT',
                basetype='EXPRESSION',
                transition=[
                    'NUMBER'
                ]
            )
        )

        # GRAMMAR_WILD
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR_WILD',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'MATCH_NEXT',
                    'MATCH_BEFORE',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'RULE_END'
                ]
            )
        )

        # GRAMMAR_OR
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR_OR',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'MATCH_NEXT',
                    'MATCH_BEFORE',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD'
                ]
            )
        )

        # VARIABLE_IDENTIFIER
        self.automata.add_state(
            AbstractAutomata(
                state='VARIABLE_IDENTIFIER',
                basetype='EXPRESSION',
                transition=[
                    'STRING'
                ]
            )
        )

        # VARIABLE_ASSIGNMENT
        self.automata.add_state(
            AbstractAutomata(
                state='VARIABLE_ASSIGNMENT',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'MATCH_NEXT',
                    'MATCH_BEFORE',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'RULE_BEGIN',
                    'RULE_END',
                    'GRAMMAR_OR'
                ]
            )
        )

        # COMMENT
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR',
                basetype='EXPRESSION',
                transition=[
                    'STRING',
                    'NUMBER',
                    'SPACE',
                    'RULE_BEGIN',
                    'RULE_END',
                    'MATCH_NEXT',
                    'MATCH_BEFORE',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'GRAMMAR_OR',
                    'VARIABLE_IDENTIFIER',
                    'VARIABLE_ASSIGNMENT',
                    'COMMENT'
                ]
            )
        )

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def get_automata(self):
        return self.automata
