questions = ["What is 5 + 3?", "What is the capital of France?", "What is 10 - 4?"]
answers = ["8", "paris", "6"]
score = 0
for i in range(len(questions)):
    print(questions[i])
    player_answer = input("Your answer: ").lower()
    if player_answer == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong! The answer was {answers[i]}.")