#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomata
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
                    'GRAMMAR_OR',
                    'MATCH_BEFORE',
                    'NUMBER',
                    'RULE_END',
                    'SPACE',
                    'STRING',
                    'VARIABLE_ASSIGNMENT',
                    'VARIABLE_IDENTIFIER'
                ]
            )
        )

        # NUMBER
        self.automata.add_state(
            AbstractAutomata(
                state='NUMBER',
                basetype='LITERAL',
                transition=[
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'MATCH_ALWAYS',
                    'MATCH_NOT',
                    'NUMBER',
                    'RULE_END',
                    'SPACE',
                    'STRING',
                    'VARIABLE_ASSIGNMENT'
                ]
            )
        )

        # SPACE
        self.automata.add_state(
            AbstractAutomata(
                state='SPACE',
                basetype='LITERAL',
                transition=[
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'NUMBER',
                    'RULE_END',
                    'SPACE',
                    'STRING',
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
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'MATCH_ALWAYS',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'MATCH_NOT',
                    'NUMBER',
                    'STRING',
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
                    'NUMBER',
                    'STRING'
                ]
            )
        )

        # MATCH_ALWAYS
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_ALWAYS',
                basetype='EXPRESSION',
                transition=[
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'MATCH_NOT',
                    'NUMBER',
                    'SPACE',
                    'STRING'
                ]
            )
        )

        # MATCH_NOT
        self.automata.add_state(
            AbstractAutomata(
                state='MATCH_NOT',
                basetype='EXPRESSION',
                transition=[
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'NUMBER',
                    'SPACE',
                    'STRING'
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
                    'GRAMMAR_HAT',
                    'MATCH_ALWAYS',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'MATCH_NOT',
                    'NUMBER',
                    'RULE_END',
                    'SPACE',
                    'STRING'
                ]
            )
        )

        # GRAMMAR_OR
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR_OR',
                basetype='EXPRESSION',
                transition=[
                    'GRAMMAR_HAT',
                    'GRAMMAR_WILD',
                    'MATCH_ALWAYS',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'MATCH_NOT',
                    'NUMBER',
                    'SPACE',
                    'STRING'
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
                    'GRAMMAR_HAT',
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'MATCH_ALWAYS',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'MATCH_NOT',
                    'NUMBER',
                    'RULE_BEGIN',
                    'RULE_END',
                    'SPACE',
                    'STRING'
                ]
            )
        )

        # COMMENT
        self.automata.add_state(
            AbstractAutomata(
                state='GRAMMAR',
                basetype='EXPRESSION',
                transition=[
                    'COMMENT',
                    'GRAMMAR_HAT',
                    'GRAMMAR_OR',
                    'GRAMMAR_WILD',
                    'MATCH_ALWAYS',
                    'MATCH_BEFORE',
                    'MATCH_NEXT',
                    'MATCH_NOT',
                    'NUMBER',
                    'RULE_BEGIN',
                    'RULE_END',
                    'SPACE',
                    'STRING',
                    'VARIABLE_ASSIGNMENT',
                    'VARIABLE_IDENTIFIER'
                ]
            )
        )

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def get_automata(self):
        return self.automata
