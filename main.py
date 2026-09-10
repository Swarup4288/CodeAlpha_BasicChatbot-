def chatbot():
    print("=" * 40)
    print("      WELCOME TO BASIC CHATBOT")
    print("=" * 40)

    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            print("\nThanks for chatting!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()