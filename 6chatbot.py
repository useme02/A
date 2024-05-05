import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"(.*) technical support",
        ["For technical support, please visit our support portal at support.example.com or contact us at support@example.com."]
    ],
    [
        r"(.*) sales department",
        ["For sales inquiries, please contact our sales team at sales@example.com."]
    ],
    [
        r"(.*) billing issue|payment problem",
        ["For billing issues or payment problems, please contact our billing department at billing@example.com."]
    ],
    [
        r"(.*) product information",
        ["For information about our products, please visit our website at www.example.com/products or contact us at info@example.com."]
    ],
    [
        r"(.*) website down|site not working",
        ["If the website is down or not working, please contact our technical support team at support@example.com."]
    ],
    [
        r"(.*) forgot password",
        ["If you forgot your password, you can reset it by visiting our password reset page at www.example.com/reset-password."]
    ],
    [
        r"(.*) network issue",
        ["If you are experiencing network issues, please contact our network operations center at noc@example.com."]
    ],
    [
        r"(.*) security concern",
        ["For security concerns, please contact our security team at security@example.com."]
    ],
]


# Create a chatbot
chatbot = Chat(pairs, reflections)

def main():
    print("Welcome to the NLTK Chatbot!")
    print("Type 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    main()
