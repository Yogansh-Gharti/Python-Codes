from datetime import datetime

CHAT_HISTORY = "chat_history.txt"

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I'm TerminalBot, your Python chatbot.",
    "python": "Python is an easy, powerful and versatile programming language.",
    "github": "GitHub is the best place to host and share your code.",
    "weather": "I can't check live weather yet, but you can build that using an API.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! 😊",
    "help": "Ask me about Python, GitHub, programming, or greet me!"
}


def chatbot(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return responses[key]

    return (
        "Sorry, I don't know the answer to that yet. "
        "Try asking something else."
    )


print("=" * 50)
print("        TERMINAL AI CHATBOT")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    reply = chatbot(user)

    print("Bot:", reply)

    with open(CHAT_HISTORY, "a") as file:
        file.write(
            f"[{datetime.now()}]\n"
            f"You : {user}\n"
            f"Bot : {reply}\n\n"
        )

print("\n✅ Chat History Saved!")
