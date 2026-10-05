import random
my_number = int(input("Think of a number between 1 and 100, then type it here:"))
computer_number = random.randint(1,100)
low = 1
high = 100
computer_guess = (low + high) // 2
turn = "computer"
low2 = 1
high2 = 100
while True:
    if turn == "computer":
        print(f"Computer guesses: {computer_guess}")
        response = input("Type 'h' if too high, 'l' if too low, or 'c'c if correct: ").lower()
        if response == "c":
            print(f"The computer guessed it! Your number was {computer_guess}.")
            break
        elif response == "h":
            high = computer_guess - 1
            computer_guess = (low + high) // 2
        elif response == "l":
            low = computer_guess + 1
            computer_guess = (low + high) // 2
        turn = "player"
    elif turn == "player":
        player_guess = int(input("Guess the computer's number: "))
        if player_guess == computer_number:
            print("You guessed it! You win!")
            break
        elif player_guess < computer_number:
            print("Too low!")
            low2 = player_guess + 1
        else:
            print("Too high!")
            high2 = player_guess - 1
        turn = "computer"

