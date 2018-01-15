#!/usr/bin/env python

from src.abstract.automata.automata import AbstractAutomata
from src.abstract.automata.automata import AbstractAutomataMachine

import unittest

class TestAutomata(unittest.TestCase):
    '''
    : unit tests for automata class.
    '''

    def test_automata_empty(self):
        automata = AbstractAutomata()
        self.assertTrue(isinstance(automata, AbstractAutomata))

    def test_machine_length_zero(self):
        machine = AbstractAutomataMachine()
        self.assertEqual(len(machine), 0)

    def test_machine_length_one(self):
        machine = AbstractAutomataMachine()
        self.assertEqual(len(machine), 0)
        machine.add_state(AbstractAutomata())
        self.assertEqual(len(machine), 1)

    def test_machine_states(self):
        machine = AbstractAutomataMachine()
        a = AbstractAutomata(
            state='A', transition=['B','C'],
            basetype='STRING')
        b = AbstractAutomata(
            state='B', transition=['B','C'],
            basetype='STRING')
        c = AbstractAutomata(
            state='C', transition=['A'],
            basetype='STRING')
        machine.add_state(a)
        machine.add_state(b)
        machine.add_state(c)
        states = machine.get_states()
        self.assertEqual(states, ['A','B','C'])

    def test_machine_transition_a(self):
        machine = AbstractAutomataMachine()
        a = AbstractAutomata(
            state='A', transition=['B','C'],
            basetype='STRING')
        b = AbstractAutomata(
            state='B', transition=['B','C'],
            basetype='STRING')
        c = AbstractAutomata(
            state='C', transition=['A'],
            basetype='STRING')
        machine.add_state(a)
        machine.add_state(b)
        machine.add_state(c)
        states = machine.get_transition('A')
        self.assertEqual(states, ['B','C'])

    def test_machine_transition_b(self):
        machine = AbstractAutomataMachine()
        a = AbstractAutomata(
            state='A', transition=['B','C'],
            basetype='STRING')
        b = AbstractAutomata(
            state='B', transition=['B','C'],
            basetype='STRING')
        c = AbstractAutomata(
            state='C', transition=['A'],
            basetype='STRING')
        machine.add_state(a)
        machine.add_state(b)
        machine.add_state(c)
        states = machine.get_transition('B')
        self.assertEqual(states, ['B','C'])

    def test_machine_transition_c(self):
        machine = AbstractAutomataMachine()
        a = AbstractAutomata(
            state='A', transition=['B','C'],
            basetype='STRING')
        b = AbstractAutomata(
            state='B', transition=['B','C'],
            basetype='STRING')
        c = AbstractAutomata(
            state='C', transition=['A'],
            basetype='STRING')
        machine.add_state(a)
        machine.add_state(b)
        machine.add_state(c)
        states = machine.get_transition('C')
        self.assertEqual(states, ['A'])

    def test_machine_transitions(self):
        machine = AbstractAutomataMachine()
        a = AbstractAutomata(
            state='A', transition=['B','C'],
            basetype='STRING')
        b = AbstractAutomata(
            state='B', transition=['B','C'],
            basetype='STRING')
        c = AbstractAutomata(
            state='C', transition=['A'],
            basetype='STRING')
        machine.add_state(a)
        machine.add_state(b)
        machine.add_state(c)
        states = machine.get_transitions()
        self.assertEqual(states, [['B', 'C'], ['B', 'C'], ['A']])
