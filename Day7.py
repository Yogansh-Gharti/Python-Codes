questions = [
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    },
    {
        "question": "Which language is used for Data Science most commonly?",
        "answer": "python"
    },
    {
        "question": "What is the capital of India?",
        "answer": "new delhi"
    },
    {
        "question": "How many continents are there on Earth?",
        "answer": "7"
    },
    {
        "question": "Who developed Python?",
        "answer": "guido van rossum"
    }
]

score = 0

print("===== PYTHON QUIZ APP =====")

name = input("Enter Your Name: ")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}:")
    print(q["question"])

    user_answer = input("Your Answer: ").strip().lower()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}")

percentage = (score / len(questions)) * 100

print("\n===== QUIZ RESULT =====")
print(f"Name: {name}")
print(f"Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 50:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")
