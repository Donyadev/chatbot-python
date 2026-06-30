# DONA CHATBOT
# Version 3.0

import datetime
import random
import json
from json import JSONDecodeError
from logging import exception


# Show menu
def show_menu():
    print("=============")
    print("DONA CHATBOT")
    print("=============")
    print()
    print("Hello!")
    print("I'm DonaBot.")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.")

def handle_command(get_word,historylist):
    greeting = ["hello", "hi", "hey", "good morning", "good evening"]

    if get_word in greeting:
       return show_hi()
    elif get_word == "how are you":
       return "I'm fine, thanks!"
    elif get_word == "help":
       return show_help()
    elif get_word == "thank you":
       return "You're welcome!"
    elif get_word == "creator":
       return "I was created by Dona :)"
    elif get_word == "your name":
       return "I'm DonaBot. :)"
    elif get_word == "time":
       return show_time()
    elif get_word == "date":
       return show_date()
    elif get_word == "joke":
       return show_joke()
    elif get_word == "history":
       return show_history(historylist)
    elif get_word in ["bye", "good bye", "exit"]:
       return "Good Bye!"
    elif get_word == "clear history":

       return clear_history(historylist)
    else:
       return "none"

def show_hi():
    greeting_answer = ["Hi!", "Hello!", "Hey there!", "Nice to see you!", "Hi! How can I help you?"]
    return random.choice(greeting_answer)

def show_help():
    botlist = ["greeting", "how are you", "help", "your name", "bye", "creator", "exit", "thank you","date","time","joke","history","clear history"]
    text=""
    for i in botlist:
        text += f"- {i}\n"
    return text

def show_date():
    x = datetime.datetime.now()
    return "Today's date is: " + x.strftime("%A") + ", " + x.strftime("%Y") + "/" + x.strftime("%m") + "/" + x.strftime("%d")

def show_time(timestamp=False):
    current_time = datetime.datetime.now()
    if not timestamp:
        return "Current time: "+ current_time.strftime("%H") + ":" + current_time.strftime("%M") + ":" + current_time.strftime("%S")
    elif timestamp:
        return  current_time.strftime("%H") + ":" + current_time.strftime("%M") + ":" + current_time.strftime("%S")


def show_joke():
    jokelist=["Why do programmers prefer dark mode? Because light attracts bugs!","Why did the computer go to the doctor? Because it had a virus!","Why was the math book sad? Because it had too many problems.","I would tell you a UDP joke... but you might not get it."]
    joke = random.choice(jokelist)
    return joke

def show_history(historylist):
    if not historylist:
        return "History is empty."

    text = "========== Chat History ==========\n\n"

    for info in historylist:
        text += f"You: {info['user']}\n"
        text += f"Bot: {info['bot']}\n\n"

    return text

def save_history(historylist):
    try:
        with open("history.json","w",encoding="utf-8") as file:
            json.dump(historylist,file,indent=4)
    except Exception:
        raise

def load_history():
    try:
        with open("history.json", "r", encoding="utf-8") as file:
          loaded_history =  json.load(file)
          return loaded_history

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def clear_history(historylist):
    try:
        historylist.clear()
        with open("history.json","w",encoding="utf-8") as file:
            json.dump(historylist,file)
        return "History cleared successfully."
    except Exception:
        raise



def main(historylist):
    loaded_histoy= load_history()
    if loaded_histoy:
        historylist= loaded_histoy
    while True:
        conversation = {}

        get_word = input("You: ").strip().lower()
        answer = handle_command(get_word, historylist)
        if answer == "none":
            print("Bot: Sorry, I don't understand.")
            conversation["user"] = get_word
            conversation["bot"] = "Sorry, I don't understand."
            conversation["time"] = show_time(timestamp=True)
            historylist.append(conversation)
            save_history(historylist)
        elif answer== "Good Bye!":
            print("Bot: Good Bye!")
            break
        elif get_word == "help" or get_word == "history":
            print(f"Bot: {answer}")

        else:
            print(f"Bot: {answer}")
            conversation["user"] = get_word
            conversation["bot"] = answer
            conversation["time"] = show_time(timestamp=True)
            historylist.append(conversation)
            save_history(historylist)


#==============
#=====Main=====
#==============

show_menu()
historylist = []

main(historylist)

