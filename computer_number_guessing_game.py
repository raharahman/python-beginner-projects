secret_number = int(input("Think of a number between 1 and 100, then type it here: "))
low = 1
high = 100
guess = (low + high) // 2
while True:
 print(f"Is your number {guess}?")
 response = input("Type 'h'h if too high, 'l' if too low, or 'c' if correct: ").lower()

 if response == "c":
       print(f"I guessed it! Your number was {guess}.")
       break
 elif response == "h":
       high = guess - 1
 elif response == "l":
       low = guess + 1
 guess = (low + high) // 2

