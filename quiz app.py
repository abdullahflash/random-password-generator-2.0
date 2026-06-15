print("Welcome to the quiz app")
score = 0

questions = [
    "Which club does Lamine Yamal play for?",
    "Which programming language are you currently learning?",
    "Who won the Ballon d'Or in 2025?",
    "What does CPU stand for?",
    "Which company owns GitHub?",
    "What data structure follows the Last In First Out (LIFO) principle?",
    "Which country will host the opening match of the 2026 FIFA World Cup?"
]

answers = [
    "barcelona",
    "python",
    "dembele",
    "central processing unit",
    "microsoft",
    "stack",
    "mexico"
]

for i in range(len(questions)):
    print(f"\nquestion{i+1}")
    useranswer = input(questions[i]).lower()
    if useranswer == answers[i]:
        print("correct!!")
        score += 1
    else:
        print("wrong!!")
        print(f"the correct answer is :{answers[i]}")

print(f"your final  score is:{score}/{len(questions)}")
percentage = score/(len(questions))*100
print(f"Your percentage is: {round(percentage, 2)}%")