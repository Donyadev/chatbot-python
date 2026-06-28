# DONA CHATBOT
# Version 1.0

print("=============")
print("DONA CHATBOT")
print("=============")


print("Hello!")
print("I'm DonaBot.")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")

botlist=["hello","hi","how are you","help","your name","bye","creator","exit","thank you"]

while True:
    get_word=input("You:").strip().lower()

    if get_word=="hello" or get_word=="hi" or get_word=="hey" or get_word=="good morning" or get_word=="good evening":
        print("Bot: Hi!")
    elif get_word=="how are you":
        print("Bot: I'm fine, thanks!")
    elif get_word=="help":
        for i in botlist:
            print(f"-{i}")
    elif get_word == "thank you":
        print("Bot: You're welcome!")
    elif get_word == "creator":
            print("Bot: I was created by Dona :)")
    elif get_word == "your name":
            print("Bot: I'm DonaBot. :)")
    elif get_word=="bye" or get_word=="good bye" or get_word=="exit":
        print("Bot: Good Bye :)")
        break
    else:
        print("Bot: Sorry, I don't understand.")

