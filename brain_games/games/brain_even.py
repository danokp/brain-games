#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random


RANDOM_NUM_FIRST = 0
RANDOM_NUM_LAST = 1_000


def is_even(num):
    return True if num % 2 == 0 else False


def give_question_and_answer_brain_even():
    random_num = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    return random_num, correct_answer


def play_brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(give_question_and_answer_brain_even, task)
