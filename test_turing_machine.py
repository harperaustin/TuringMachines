import unittest
from turing_machine import TuringMachine

class TestTuringMachine(unittest.TestCase):

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