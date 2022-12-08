#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet
import prompt
import random


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def main():
    name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    question_num = 3

    while question_num > 0:
        random_num = random.randint(0, 1_000)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(random_num)

        if answer == correct_answer:
            print('Correct!')
            question_num -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer \
was '{correct_answer}'.\nLet's try again, {name}!")
            break
    if question_num == 0:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
