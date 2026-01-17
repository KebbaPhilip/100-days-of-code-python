import random
import ascii

EASY = 10
HARD = 5

# check difficulty
def difficuly():
    '''Sets the difficulty level and return maximum number of guesses allowed'''
    level = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        max_guess = EASY
        return max_guess
    elif level == "hard":
        max_guess = HARD
        return max_guess
    else:
        max_guess = EASY
        return max_guess


# check answer
def check_answer(guess, answer, turns_remaining):
    '''Compares answer against guess, and returns the attempts remaining.'''
    if guess > answer:
        print("Too high")
        return turns_remaining - 1
    elif guess < answer:
        print("Too low")
        return turns_remaining - 1
    else:
        print(f"You guessed right, the answer was {guess}")


def start_game():
    print(ascii.logo)
    print("*** Welcome To The Number Guessing Game ***")
    print("I'm thinking of a number between 1 and 100 ....")
    secret_answer = random.randint(1, 100)
    attempts = difficuly()

    guess = 0
    while guess != secret_answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts = check_answer(guess=user_guess, answer=secret_answer, turns_remaining=attempts)

        if attempts == 0:
            print(f"You have run out of guesses, you loose.")
            break
        elif user_guess != secret_answer:
            print("Guess again.")
        elif user_guess == secret_answer:
            break
          
start_game()