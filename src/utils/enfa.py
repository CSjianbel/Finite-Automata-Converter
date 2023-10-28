import NFA

class eNFA(NFA):
    def __init__(self, states: set[str], alphabet: set[str], start: str, final_states: set[str], transitions: dict) -> None:
        super.__init__(states, alphabet, start, final_states, transitions)
        self.alphabet.add('ε')

    
