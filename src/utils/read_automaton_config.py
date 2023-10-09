from .automata import Automata

class ReadAutomataConfig:

    def __init__(self, path: str) -> None:
        self.path = path
        
    def read_config(self) -> Automata or None:
        alphabet = ['ε']
        with open(self.path, 'r', encoding='utf-8') as config:
            states = config.readline().strip().split(':')[1].strip().split(' ')
            alphabet.extend(config.readline().strip().split(':')[1].strip().split(' '))
            start = config.readline().strip().split(':')[1]
            final_states = config.readline().strip().split(':')[1].strip().split(' ')

            transition_table = {state: {symbol: [] for symbol in alphabet} for state in states}
            transitions = config.readlines()[1:]
            for transition in transitions:
                if transition.isspace():
                    break
                transition = transition.strip()
                state, symbol = transition.split(':')[0].strip().split(' ')                
                reachable_state = transition.split(':')[1].strip()
                transition_table[state][symbol].append(reachable_state)
            
            return Automata(states, alphabet, transition_table, start, final_states)



