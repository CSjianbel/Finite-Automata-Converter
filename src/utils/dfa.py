from automata import Automata

class DFA(Automata):

    def __init__(self, states: set[str], alphabet: set[str], start: str, final_states: set[str], transitions) -> None:
        super().__init__(states, alphabet, start, final_states)
        # delta(q, a) = s
        self.transitions = transitions
    
    def delta(self, q: str, a: str):
        return self.transitions[q][a]

    def is_in_language(self, input: str):
        current = self.start
        for symbol in input:
            current = self.delta(current, symbol)

        return current in self.final_states
    
    def __str__(self):
        return super().__str__() + f'Transitions: {self.transitions}'
