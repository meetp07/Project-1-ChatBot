import random
from fuzzywuzzy import fuzz
from datetime import datetime

# ANSI escape codes for text colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
LIGHT_PURPLE = "\033[1;35m"
RESET = "\033[0m"

# This function is used to ask the user for a question
def questions():
    print("\nPlease select a number according to your question")
    print("1. Who are you?")
    print("2. What can you do?")
    print("3. How are you?")
    print("4. Tell me a joke?")
    print("5. Exit\n")

# This function is used to greet the user according to the current time
def greet():
    # This will check the current time
    current_time = datetime.now().time()
    # If the current time is morning, then it will say good morning
    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        print(f"{YELLOW}Good morning! ☀️ \nI'm your friendly chatbot. I can solve your problems{RESET}")
    # If the current time is afternoon, then it will say good afternoon
    elif current_time < datetime.strptime("18:00:00", "%H:%M:%S").time():
        print(f"{YELLOW}Good afternoon! 🌤️ \nI'm your friendly chatbot. I can solve your problems{RESET}")
    # If the current time is night, then it will say good evening
    else:
        print(f"{YELLOW}Good evening! 🌙 \nI'm your friendly chatbot. I can solve your problems{RESET}")

# This function is used to say goodbye to the user
def farewell():
    print(f"{YELLOW}\nGoodbye! 👋 \nIf you have more questions, feel free to ask.{RESET}")

def get_similarity(input_str, target_str):
    return fuzz.ratio(input_str.lower(), target_str.lower())

def handle_question(question):
    if get_similarity(question, "hi") >= 80:
        response = "Hello! How can I help you today?"
    elif get_similarity(question, 'who are you') >= 80:
        response = "I'm a chatbot designed to assist you."
    elif get_similarity(question, 'what can you do') >= 80:
        response = "I can answer your questions and engage in simple conversations."
    elif get_similarity(question, 'how are you') >= 80:
        response = "I'm always fine because I'm just a computer program, but thanks for asking! 😊"
    elif get_similarity(question, 'tell me a joke') >= 80:
        jokes = ["Why did the computer go to therapy? It had too many bytes of emotional baggage.",
                 "Why was the math book sad? Because it had too many problems.",
                 "I told my computer I needed a break, and now it won't stop sending me vacation ads."
                 "Why don't oysters donate to charity? Because they are shellfish.",
                 "I used to be a baker because I kneaded dough.",
                 "I told my wife she should embrace her mistakes. She gave me a hug."]
        response = random.choice(jokes)
    elif get_similarity(question, 'exit') >= 80:
        farewell()
        exit()
    else:
        return f"{LIGHT_PURPLE}I'm sorry, I didn't understand that. Can you please ask another question? or do you want to exit?{RESET}"

    # Ask the user if the response is what they intended        
    user_response = input(f"{GREEN}Bot: {BLUE}{response}\n{YELLOW}Did you mean to ask that? (yes/no): {RESET}").lower()

    def response(user_response):
        if user_response == 'yes':
            return f"{BLUE}Thank you!, You can ask more or exit.{RESET}"
        elif user_response == 'no':
            return f"{RED}I apologize. Please ask your question again or exit.{RESET}"
        else:
            return f"{LIGHT_PURPLE}I'm sorry, I didn't understand your response. Please answer with 'yes' or 'no'.{RESET}"
            response(user_response)    
    return response(user_response)
    

# This function is used to take input from the user and return the response accordingly
def chat():
    greet()  # Greeting function called
    questions()  # Questions will be displayed
    while True:  # Run until the user responds exit
        user_input = input(f"{YELLOW}You: {RESET}").lower()
        user_input = user_input.strip(",.?/'}{!@#$%^&*()") # remove extera characters from user input
        response = handle_question(user_input)
        print(f"{GREEN}Bot:{RESET} {response}")

    farewell()  # Farewell function called

# Main Function
if __name__ == "__main__":
    chat()