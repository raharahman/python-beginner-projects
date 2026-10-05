import random
secret_number = random.randint (1,100)
guess = None
print("I'm thinking of a number between 1 and 100.")
while guess != secret_number:
    guess = int(input("Take a guess: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Eureka, that's it!")