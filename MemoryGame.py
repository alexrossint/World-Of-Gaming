import random
import subprocess
import time
from cmath import sqrt
from logging import setLogRecordFactory


def generate_sequence(difficulty):
    sequence = []
    for _ in range(difficulty):
        number = random.randint(1, 101)
        sequence.append(number)
    return sequence

def show_sequence(sequence):
    print("Remember these numbers:")
    number_as_text = []
    for number in sequence:
        number_as_text.append(str(number))
    print(" ".join(number_as_text))
    time.sleep(0.7)
    subprocess.run("clear")

def user_answer(difficulty):
    while True:
        print()
        answer = input(f"Type the {difficulty} shown numbers separated by space: ")
        print()
        pieces = answer.split()
        numbers = []
        try:
            for piece in pieces:
                numbers.append(int(piece))
        except ValueError:
            print("Whole numbers only, separated by space. Example: 23 41 11")
            continue
        if len(numbers) != difficulty:
            print(f"You must type exactly {difficulty} numbers as shown before")
            continue
        return numbers

def check_answer(sequence, answer):
    return sequence == answer

def play(difficulty):
    sequence = generate_sequence(difficulty)
    show_sequence(sequence)
    answer = user_answer(difficulty)
    return check_answer(sequence, answer)