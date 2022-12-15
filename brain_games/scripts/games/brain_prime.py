#!/usr/bin/env python3
from brain_games.scripts.brain_games_functions import play_game
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


def give_question_and_answer_brain_prime():
    random_num_first = 0
    random_num_last = 1_000
    random_num = random.randint(random_num_first, random_num_last)
    correct_answer = is_prime(random_num)
    return random_num, correct_answer


def main():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(give_question_and_answer_brain_prime, task)


if __name__ == '__main__':
    main()
