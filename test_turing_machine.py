import unittest
from turing_machine import TuringMachine

class TestTuringMachine(unittest.TestCase):

    # TODO: test more.
    def test_scenario_1(self):
        # Create a machine that accepts the language of all strings with an even number of a's
        machine = TuringMachine(
            input_alphabet=['a', 'b'],
            tape_alphabet=['a', 'b', 'X', ' '],
            states=['q0', 'q1', 'q2', 'qaccept', 'qreject'],
            start_state='q0',
            accept_state='qaccept',
            reject_state='qreject',
            transition_function={
                ('q0', 'a'): ('q1', 'X', 'R'),
                ('q0', 'b'): ('q2', 'X', 'R'),
                ('q0', ' '): ('qaccept', ' ', 'S'),
                ('q1', 'a'): ('q2', 'a', 'R'),
                ('q2', 'a'): ('q1', 'a', 'R'),
                ('q1', 'b'): ('q1', 'b', 'R'),
                ('q2', ' '): ('qaccept', 'X', 'S'),
                ('q2', 'b'): ('q2', 'b', 'R'),
                ('q1', ' '): ('qreject', ' ', 'S'),
            }
        )
        self.assertTrue(machine.run("aa"))
        self.assertFalse(machine.run("a"))
        self.assertTrue(machine.run("b"))
        self.assertFalse(machine.run("ab"))
        self.assertFalse(machine.run("ba"))
        self.assertTrue(machine.run(""))
        self.assertTrue(machine.run("aabaaaa"))
        self.assertTrue(machine.run("aabbaa"))
        self.assertFalse(machine.run("aabbba"))
        self.assertFalse(machine.run("aabbba"))
        self.assertFalse(machine.run("aaabbb"))
        self.assertFalse(machine.run("abbb"))


    def test_invalid_transition(self):
        # Create a machine with invalid transition
        invalid_machine = TuringMachine(
            input_alphabet=['a', 'b'],
            tape_alphabet=['a', 'b', ' '],
            states=['q0', 'qaccept', 'qreject'],
            start_state='q0',
            accept_state='qaccept',
            reject_state='qreject',
            transition_function={
                ('q0', 'a'): ('invalid_state', 'a', 'R')  # Invalid state
            }
        )
        with self.assertRaises(ValueError):
            invalid_machine.run("a")

    def test_invalid_direction(self):
        # Create a machine with invalid direction
        invalid_machine = TuringMachine(
            input_alphabet=['a'],
            tape_alphabet=['a', ' '],
            states=['q0', 'qaccept', 'qreject'],
            start_state='q0',
            accept_state='qaccept',
            reject_state='qreject',
            transition_function={
                ('q0', 'a'): ('qaccept', 'a', 'U')  # Invalid direction
            }
        )
        with self.assertRaises(ValueError):
            invalid_machine.run("a")

if __name__ == '__main__':
    unittest.main() 