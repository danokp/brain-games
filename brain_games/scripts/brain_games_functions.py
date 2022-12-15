#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_one_round(name, question, correct_answer, question_num):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        question_num -= 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer \
was '{correct_answer}'.\nLet's try again, {name}!")
        question_num = -1
    return question_num


def congratulate_winner(name, question_num):
    if question_num == 0:
        print(f'Congratulations, {name}!')


def play_game(game_name, task):
    name = welcome_user()
    print(task)
    question_num = 3
    while question_num > 0:
        question, correct_answer = game_name()
        question_num = play_one_round(name,
                                      question,
                                      correct_answer,
                                      question_num)
    congratulate_winner(name, question_num)
