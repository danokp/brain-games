#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random


RANDOM_NUM_FIRST = 0
RANDOM_NUM_LAST = 1_000


def is_prime(num):
    if num > 1:
        count_div = 1
        for i in range(1, int(num // 2 + 1)):
            if num % i == 0:
                count_div += 1
            if count_div > 2:
                return False
        return True
    else:
        return False


def give_question_and_answer_brain_prime():
    random_num = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    correct_answer = 'yes' if is_prime(random_num) else 'no'
    return random_num, correct_answer


def play_brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(give_question_and_answer_brain_prime, task)
