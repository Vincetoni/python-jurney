import random

def guessing_game():
    secret_number= random.randint(1,100)
    atempt=0

    print('welcome to vincetoni guessing game')
    print('im think of a number from 1 to 100')

    while True:
        user_input= input('guess the number:')

        if not user_input.isdigit():
            print('input a number')
            continue

        guess = int(user_input)
        atempt +=1

        if guess > secret_number:
            print('too high goo lower ')
        elif guess < secret_number:
            print('too low go higher')
        else:
            print(f'🥰 congratulation you guessed the secret number: {secret_number} in {atempt} tries')
            break


guessing_game()