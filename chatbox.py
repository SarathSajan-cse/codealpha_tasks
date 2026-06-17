
def chatbox_reply(user):
    if "hello" in user:
        return "HI"
    elif "how are you" in user:
        return "I Am Fine Thanks"
    elif "name" in user:
        return "I Am Your Python Chatbox "
    elif "time" in user:
        import time
        return f"Current time is {time.ctime()}"
    elif user == "bye":
        return "Goodbye"
    else:
        return "I Dont Understand"
name = input("Enter Your Name: ")
print(f"\nHi {name}! I Am Your Python Chatbox. Type 'bye' to exit\n")
while True:
    user=input("You: ").lower()
    reply = chatbox_reply(user)
    print("Bot: ",reply)
    if user == "bye":
        break