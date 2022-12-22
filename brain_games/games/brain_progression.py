#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random

PROG_DIFF_RANDOM_FIRST = 1
PROG_DIFF_RANDOM_LAST = 10
PROG_START_RANDOM_FIRST = 0
PROG_START_RANDOM_LAST = 100
PROG_LEN_RANDOM_FIRST = 5
PROG_LEN_RANDOM_LAST = 10
PROG_INDEX_RANDOM_FIRST = 0


def give_question_and_answer_brain_progression():
    random_progression_diff = random.randint(PROG_DIFF_RANDOM_FIRST,
                                             PROG_DIFF_RANDOM_LAST)
    random_progression_start = random.randint(PROG_START_RANDOM_FIRST,
                                              PROG_START_RANDOM_LAST)
    random_progression_len = random.randint(PROG_LEN_RANDOM_FIRST,
                                            PROG_LEN_RANDOM_LAST)
    prog_index_random_last = random_progression_len - 1
    random_index = random.randint(PROG_INDEX_RANDOM_FIRST,
                                  prog_index_random_last)
    progression = [str(random_progression_start + i * random_progression_diff)
                   for i in range(random_progression_len)]
    correct_answer = progression[random_index]
    question = []
    question.extend(progression[:random_index])
    question.append('..')
    question.extend(progression[random_index + 1:])
    return ' '.join(question), str(correct_answer)


def play_brain_progression():
    task = 'What number is missing in the progression?'
    play_game(give_question_and_answer_brain_progression, task)
