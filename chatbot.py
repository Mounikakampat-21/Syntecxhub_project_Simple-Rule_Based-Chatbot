import re

# -----------------------------
#   SIMPLE RULE-BASED CHATBOT
# -----------------------------

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting patterns
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today?"

    # Small talk
    elif "how are you" in user_input:
        return "I'm doing great! What about you?"

    elif "your name" in user_input:
        return "I am SyntecxBot, your simple rule-based chatbot."

    # Help intent
    elif "help" in user_input:
        return "Sure! Tell me what you need help with."

    # Domain knowledge base
    elif "python" in user_input:
        return "Python is a powerful programming language used for AI, ML, and web development."

    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "AI means machines that can learn and make decisions like humans."

    elif "machine learning" in user_input:
        return "Machine Learning helps computers learn patterns from data."

    # Goodbye intent
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "I’m not sure I understood that. But I am learning!"


# -----------------------------
#       MAIN CHAT LOOP
# -----------------------------
print("🤖 Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Bye! Have a nice day ❤️")
        break

    response = get_response(user_input)
    print("Chatbot:", response)
