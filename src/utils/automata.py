
class Automata: 

    def __init__(self, states: list[str], alphabet: list[str], transition_table: dict, start: str, final_states: list[str]) -> None:
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start = start
        self.final_states = final_states


    def __str__(self):
        return f'Automata Definition:\nStates: {self.states}\nAlphabet: {self.alphabet}\nStart State: {self.start}\nFinal states: {self.final_states}\nTransition_table:\n{self.transition_table}'
    
