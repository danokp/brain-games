#!/usr/bin/env python3
from brain_games.scripts.brain_games_functions import (welcome_user,
                                                       play_game,
                                                       congratulate_winner)
import random


def is_prime(num):
    if num > 1:
        count_div = 1
        for i in range(1, int(num // 2 + 1)):
            if num % i == 0:
                count_div += 1
            if count_div > 2:
                return 'no'
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    question_num = 3
    while question_num > 0:
        random_num_first = 0
        random_num_last = 1_000
        random_num = random.randint(random_num_first, random_num_last)
        correct_answer = is_prime(random_num)
        question_num = play_game(name, random_num, correct_answer, question_num)

    congratulate_winner(name, question_num)


if __name__ == '__main__':
    main()
