from collections import defaultdict


class TuringMachine:
    # initialize the turing machine
    def __init__(self, input_alphabet : list[str], tape_alphabet : list[str], states : list[str], start_state : str, accept_state : str, reject_state : str, transition_function : dict[tuple[str, str], tuple[str, str, str]]):
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        # verify that input alphabet is a subset of tape alphabet
        for symbol in input_alphabet:
            if symbol not in tape_alphabet:
                raise ValueError(f"Symbol {symbol} is in the input alphabet but not in the tape alphabet")
        self.states = states
        # verify that start state is in states
        if start_state not in states:
            raise ValueError(f"Start state {start_state} is not in the states")
        self.start_state = start_state
        # verify that accept state is in states
        if accept_state not in states:
            raise ValueError(f"Accept state {accept_state} is not in the states")
        self.accept_state = accept_state
        # verify that reject state is in states
        if reject_state not in states:
            raise ValueError(f"Reject state {reject_state} is not in the states")
        self.reject_state = reject_state
        # verify that transition function is a dictionary
        if not isinstance(transition_function, dict):
            raise ValueError("Transition function must be a dictionary")
        self.transition_function = transition_function



    # run the turing machine on an input string
    def run(self, input_string: str):
        tape = defaultdict(lambda: " ")
        for i, symbol in enumerate(input_string):
            if symbol not in self.input_alphabet:
                raise ValueError(f"Symbol {symbol} is not in the input alphabet")
            tape[i] = symbol
        current_state = self.start_state
        head_position = 0  # Start at the beginning of the tape
        
        while current_state != self.accept_state and current_state != self.reject_state:
            current_state, head_position = self.step(current_state, tape, head_position)
            
        if current_state == self.accept_state:
            return True
        else:
            return False
        


    # step the turing machine
    def step(self, current_state : str, tape : dict[int, str], head_position : int) -> tuple[str, int]:
        if current_state not in self.states:
            raise ValueError(f"Current state {current_state} is not in the states")
            
        current_symbol = tape[head_position]
        if (current_state, current_symbol) not in self.transition_function:
            raise ValueError(f"No transition defined for state {current_state} and symbol {current_symbol}")
            
        new_state, new_symbol, direction = self.transition_function[(current_state, current_symbol)]
        if new_state not in self.states:
            raise ValueError(f"New state {new_state} is not in the states")
        if new_symbol not in self.tape_alphabet:
            raise ValueError(f"New symbol {new_symbol} is not in the tape alphabet")
        if direction not in ['R', 'L', 'S']:
            raise ValueError(f"Invalid direction {direction}. Must be 'L', 'R', or 'S'")
        
        # Write the new symbol to the tape
        tape[head_position] = new_symbol
        
        # Move the head
        if direction == 'R':
            head_position += 1
        elif direction == 'L':
            head_position -= 1
        # 'S' means stay in place, so no change to head_position
            
        return new_state, head_position
