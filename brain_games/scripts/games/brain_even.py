#!/usr/bin/env python3
from brain_games.scripts.brain_games_functions import play_game
import random


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def give_question_and_answer_brain_even():
    random_num_first = 0
    random_num_last = 1_000
    random_num = random.randint(random_num_first, random_num_last)
    correct_answer = is_even(random_num)
    return random_num, correct_answer


def main():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(give_question_and_answer_brain_even, task)


if __name__ == '__main__':
    main()
