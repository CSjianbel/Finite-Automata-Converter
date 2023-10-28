import Automata

class NFA(Automata):

    def __init__(self, states: set[str], alphabet: set[str], start: str, final_states: set[str], transitions: dict) -> None:
        super.__init__(states, alphabet, start, final_states)
        # delta(q, a) = {s_1, s_2, ... s_n}
        self.transitions = transitions

    def __str__(self):
        return super.__str__() + f'\n\nTransitions: {self.transitions}'