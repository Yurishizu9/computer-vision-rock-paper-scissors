import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    user_input = input('Choose between "Rock", "Paper", "Scissors"')
    return user_input
    