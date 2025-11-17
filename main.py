import responses

print("\nWelcome to Karan's Mini AI Chatbot!")
print("--------------------------------------")

name = input("What's your name? ")
print(f"Hello {name}, how can I help you today?")

while True:
    user_input = input("\nYou: ").lower()

    if user_input in ["exit", "quit", "bye"]:
        print("AI: It was nice talking to you! Goodbye ❤️")
        break

    response = responses.get_response(user_input)
    print("AI:", response)
