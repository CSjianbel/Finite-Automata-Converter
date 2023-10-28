
class Automata: 

    def __init__(self, states: set[str], alphabet: set[str], start: str, final_states: set[str]) -> None:
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.final_states = final_states

    def __str__(self):
        return f'Automata Definition:\nStates: {self.states}\nAlphabet: {self.alphabet}\nStart State: {self.start}\nFinal states: {self.final_states}\n'
    
