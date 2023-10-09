# import argparse
import os

from utils.read_automaton_config import ReadAutomataConfig

TEST_DIR = os.path.join('..', 'tests')

def main():

    test1_path = os.path.join(TEST_DIR, 'test1.txt')
    reader = ReadAutomataConfig(test1_path)
    automata = reader.read_config()
    print(automata)

if __name__ == '__main__':
    main()
