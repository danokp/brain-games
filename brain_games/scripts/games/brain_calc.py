#!/usr/bin/env python3
from brain_games.scripts.brain_games_functions import (welcome_user,
                                                       play_game,
                                                       congratulate_winner)
import random


def calc_answer(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '*':
        return num_1 * num_2


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    question_num = 3
    while question_num > 0:
        random_num_1 = random.randint(0, 50)
        random_num_2 = random.randint(0, 50)
        operator = random.choice(['*', '+'])
        correct_answer = str(calc_answer(random_num_1, random_num_2, operator))
        question = f'{random_num_1} {operator} {random_num_2}'
        question_num = play_game(name, question, correct_answer, question_num)

    congratulate_winner(name, question_num)


if __name__ == '__main__':
    main()
