#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random


def calc_answer(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '-':
        return num_1 - num_2


def give_question_and_answer_brain_calc():
    random_num_first = 0
    random_num_last = 50
    random_num_1 = random.randint(random_num_first, random_num_last)
    random_num_2 = random.randint(random_num_first, random_num_last)
    operator = random.choice(['*', '+', '-'])
    correct_answer = str(calc_answer(random_num_1, random_num_2, operator))
    question = f'{random_num_1} {operator} {random_num_2}'
    return question, correct_answer


def play_brain_calc():
    task = 'What is the result of the expression?'
    play_game(give_question_and_answer_brain_calc, task)
