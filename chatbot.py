import re

def chatbot_response(user_input):
    # Convert input to lowercase for consistency
    user_input = user_input.lower()

    # Define a set of rules for predefined responses
    if re.search(r'hello|hi|hey', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'how are you', user_input):
        return "I'm doing great, thank you for asking!"
    elif re.search(r'bye|goodbye', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'what is your name', user_input):
        return "I am a simple chatbot created by you!"
    elif re.search(r'help|assist', user_input):
        return "I am here to assist you. Ask me anything!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def start_chat():
    print("Chatbot: Hi, I am your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye', user_input.lower()):
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
start_chat()
