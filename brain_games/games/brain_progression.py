#!/usr/bin/env python3
from brain_games.brain_games_engine import play_game
import random


def give_question_and_answer_brain_progression():
    prog_diff_random_first = 1
    prog_diff_random_last = 10
    random_progression_diff = random.randint(prog_diff_random_first,
                                             prog_diff_random_last)
    prog_start_random_first = 0
    prog_start_random_last = 100
    random_progression_start = random.randint(prog_start_random_first,
                                              prog_start_random_last)
    prog_len_random_first = 5
    prog_len_random_last = 10
    random_progression_len = random.randint(prog_len_random_first,
                                            prog_len_random_last)
    prog_index_random_first = 0
    prog_index_random_last = random_progression_len - 1
    random_index = random.randint(prog_index_random_first,
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
