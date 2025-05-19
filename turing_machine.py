class TuringMachine:
    def __init__(self, input_alphabet : list[str], tape_alphabet : list[str], states : list[str], start_state : str, accept_state : str, reject_state : str, transition_function : dict[str, str]):
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
        self.transition_function = transition_function
