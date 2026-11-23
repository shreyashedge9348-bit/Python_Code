# Guess the fixed secret number
secret = 42
guess = None

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
