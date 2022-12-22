#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random

RANDOM_NUM_FIRST = 0
RANDOM_NUM_LAST = 50
OPERATORS_RANGE = ['*', '+', '-']


def calc_answer(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '-':
        return num_1 - num_2


def give_question_and_answer_brain_calc():
    random_num_1 = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    random_num_2 = random.randint(RANDOM_NUM_FIRST, RANDOM_NUM_LAST)
    operator = random.choice(OPERATORS_RANGE)
    correct_answer = str(calc_answer(random_num_1, random_num_2, operator))
    question = f'{random_num_1} {operator} {random_num_2}'
    return question, correct_answer


def play_brain_calc():
    task = 'What is the result of the expression?'
    play_game(give_question_and_answer_brain_calc, task)
