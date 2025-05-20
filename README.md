# Python Turing Machine Implementation

This is a Python implementation of a Turing Machine, a theoretical computing device that can simulate any algorithm. The implementation allows for creating and running Turing Machines with custom alphabets, states, and transition functions.

## Overview

A Turing Machine consists of:

- An infinite tape divided into cells
- A head that can read and write symbols on the tape
- A set of states
- A transition function that determines the machine's behavior

The machine processes input by:

1. Starting with the input string on the tape
2. Beginning in the start state with the head over the first character of the input
3. Following the transition function until reaching an accept or reject state

## Usage

### Initialization

```python
machine = TuringMachine(
    input_alphabet: list[str],
    tape_alphabet: list[str],
    states: list[str],
    start_state: str,
    accept_state: str,
    reject_state: str,
    transition_function: dict[tuple[str, str], tuple[str, str, str]]
)
```

#### Parameters

- `input_alphabet`: List of symbols that can appear in the input string
- `tape_alphabet`: List of symbols that can appear on the tape (must include all input alphabet symbols)
- `states`: List of all possible states the machine can be in
- `start_state`: The initial state of the machine
- `accept_state`: The state that indicates the input is accepted
- `reject_state`: The state that indicates the input is rejected
- `transition_function`: Dictionary mapping (current_state, current_symbol) to (new_state, new_symbol, direction)

#### Transition Function Format

The transition function is a dictionary where:

- Keys are tuples of (current_state, current_symbol)
- Values are tuples of (new_state, new_symbol, direction)
- Direction can be:
  - 'R': Move right
  - 'L': Move left
  - 'S': Stay in place

Example:

```python
{
    ('q0', 'a'): ('q1', 'X', 'R'),  # In state q0, reading 'a': go to q1, write 'X', move right
    ('q1', 'b'): ('q2', 'Y', 'L'),  # In state q1, reading 'b': go to q2, write 'Y', move left
    ('q2', ' '): ('qaccept', ' ', 'S')  # In state q2, reading blank: accept and stay
}
```

### Running the Machine

```python
result = machine.run(input_string: str) -> bool
```

- Returns `True` if the input is accepted
- Returns `False` if the input is rejected
- Raises `ValueError` if:
  - Input contains symbols not in the input alphabet
  - Current state is not in the states list
  - No transition is defined for the current state and symbol
  - New state is not in the states list
  - New symbol is not in the tape alphabet
  - Direction is not 'R', 'L', or 'S'

## Important Notes

1. The tape is infinite in both directions, with blank spaces (' ') filling unused cells
2. The head starts over the first character of the input string, not on a blank space before it
3. The input alphabet must be a subset of the tape alphabet
4. The start state, accept state, and reject state must be in the states list
5. The transition function must be complete for all possible (state, symbol) pairs that the machine might encounter

## Example

```python
# Create a machine that accepts strings with an even number of 'a's
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
        ('q2', 'b'): ('q2', 'b', 'R'),
        ('q1', ' '): ('qreject', ' ', 'S'),
        ('q2', ' '): ('qaccept', 'X', 'S')
    }
)

# Test the machine
print(machine.run("aa"))  # True
print(machine.run("a"))   # False
print(machine.run(""))    # True
```
