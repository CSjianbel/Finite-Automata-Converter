from automata import Automata

class NFA(Automata):

    def __init__(self, states: set[str], alphabet: set[str], start: str, final_states: set[str], transitions: dict) -> None:
        super.__init__(states, alphabet, start, final_states)
        # delta(q, a) = {s_1, s_2, ... s_n}
        self.transitions = transitions

    def delta(self, q: str, a: str):
        return self.transitions[q][a]

    def is_in_language(self, input: str):
        active_states = {self.start}

        for symbol in input: 
            tmp = {}
            for state in active_states:
                tmp.union(self.delta(state, symbol))
            active_states = tmp

        return self.final_states in active_states 

    def __str__(self):
        return super.__str__() + f'\n\nTransitions: {self.transitions}'