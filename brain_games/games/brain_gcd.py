#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random


RANDOM_NUM_FIRST = 1
RANDOM_NUM_LAST = 100


def calc_gcd(num_1, num_2):
    max_num = max(num_1, num_2)
    min_num = min(num_1, num_2)
    for num in range(min_num, 0, -1):
        if min_num % num == 0:
            if max_num % num == 0:
                return num


def give_question_and_answer_brain_gcd():
    random_num_1 = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    random_num_2 = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    correct_answer = str(calc_gcd(random_num_1, random_num_2))
    question = f'{random_num_1} {random_num_2}'
    return question, correct_answer


def play_brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    play_game(give_question_and_answer_brain_gcd, task)
