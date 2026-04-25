import random

def get_valid_number(prompt, low=None, high=None):
    valid = False
    value = 0

    while not valid:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if low is not None and high is not None:
                if value >= low and value <= high:
                    valid = True
                else:
                    print(f"Please enter a number between {low} and {high}.")
            else:
                valid = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return value


def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Nivel Fácil (Easy)    (1–50, 10 attempts)")
    print("2. Nivel Medio (Medium)  (1–100, 7 attempts)")
    print("3. Nivel Difícil (Hard)  (1–500, 5 attempts)")

    valid = False
    while not valid:
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 1, 50, 10
        if choice == "2":
            return 1, 100, 7
        if choice == "3":
            return 1, 500, 5

        print("Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    low, high, max_attempts = choose_difficulty()
    number = random.randint(low, high)
    attempts = 0
    guesses = []

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts.\n")

    correct = False

    while attempts < max_attempts and not correct:
        guess = get_valid_number(f"Enter your guess ({low}-{high}): ", low, high)
        guesses.append(guess)
        attempts = attempts + 1

        if guess < number:
            print("Too low! Try a higher number.\n")
        elif guess > number:
            print("Too high! Try a lower number.\n")
        else:
            correct = True

            # ⭐ Special message for guessing correctly on the first try
            if attempts == 1:
                print("\n🤯 You just read my mind!!")

            print("\n🎉 YOU GOT IT! Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            print(f"Your guesses: {guesses}")

    if not correct:
        print("\n❌ OOPS....Out of attempts, Try again!")
        print(f"The correct number was: {number}")
        print(f"Your guesses: {guesses}")


def main():
    print("===== NUMBER GUESSING GAME =====")
    play_again = "y"

    while play_again == "y":
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()

    print("\nThanks for playing! Have a nice day !")


main()
