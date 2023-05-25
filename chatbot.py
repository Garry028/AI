import nltk
from nltk.chat.util import Chat,reflections


pairs = [
    [
        r"hi|hello|hey",
        ["Hello! welcome to redbus. how can i assist you today?"]
    ],
    [
        r"book a ticket|book|ticket",
        ["Sure! i can help you with that. Please provide source and destination address for booking the bus"]
    ],
    [
        r"cancel a ticket|cancel",
        ["I'm sorry to hear that . please provide further details to for cancelation"]
    ],
    [
        r"bus schedules?",
        ["To check bus schedules , please provide the source and destination address so that i will help you further"]
    ],
    [
        r"contact customer support|customer support|customer care|help",
        ["Our customer support team is available 24/7. you can reach them at 123-456-789 or support@redbus.com"]
    ],
    [
        r"(.*)",
        ["I'm sorry , I did't understand. How can i assist you with your redbus booking"]
    ]
]

def chat():
    print("Welcome to RedBus! How can i assist you today?")
    chatbot=Chat(pairs,reflections)
    chatbot.converse()

chat()