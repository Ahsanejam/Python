import random
from art import logo
print(logo)

def randon_number():
    return random.randint(1, 100)
rand_number = randon_number()



def game_run():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100")
    print(f"Pssst, the correct answer is {rand_number}")

    number_of_attempts = 0
    choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_level == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5

    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand_number:
            print(f"You got it! The answer was {rand_number}")
            number_of_attempts = 0

        if number_of_attempts > 1:
            if guess > rand_number:
                print("Too high.")
                print("Guess again.")

        # if number_of_attempts > 1:
            if rand_number > guess:
                print("Too low.")
                print("Guess again.")


        if number_of_attempts == 1:
            if guess != rand_number:
                if guess > rand_number:
                    print("Too high.")
                    print("You've run out of guesses, you lose.")
                else:
                    print("Too low.")
                    print("You've run out of guesses, you lose.")

        number_of_attempts -= 1

game_run()
