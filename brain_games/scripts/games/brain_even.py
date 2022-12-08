#!/usr/bin/env python3
from brain_games.scripts.brain_games_functions import (welcome_user,
                                                       play_game,
                                                       congratulate_winner)
import random


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    question_num = 3
    while question_num > 0:
        random_num = random.randint(0, 1_000)
        correct_answer = is_even(random_num)
        question_num = play_game(name, random_num, correct_answer, question_num)

    congratulate_winner(name, question_num)


if __name__ == '__main__':
    main()
