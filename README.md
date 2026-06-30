# Dona ChatBot

A console-based chatbot built with Python.

This project started as a simple chatbot and has gradually evolved by adding new features and improving the project structure.
Chat history is automatically stored in a local JSON file and automatically loaded each time the program starts.

## Features

* Responds to greetings
* Answers simple questions
* Shows available commands with `help`
* Displays the current date
* Displays the current time
* Tells random programming jokes
* Stores conversation history
* Automatically loads previous chat history
* Saves chat history to a JSON file
* Clears chat history
* Adds a timestamp to every conversation
* Handles unknown commands gracefully

## Available Commands

* hello
* hi
* hey
* good morning
* good evening
* how are you
* your name
* creator
* thank you
* help
* date
* time
* joke
* history
* clear history
* bye
* exit

## Technologies Used

* Python
* JSON
* `datetime`
* `random`

## Project Structure

```text
.
├── main.py
├── README.md
└── .gitignore
```

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Example

```text
You: hello
Bot: Hello!

You: joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: history
Bot:
========== Chat History ==========

You: hello
Bot: Hello!

You: joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!
```

## Version

**Current Version:** 3.0

### What's New in Version 3

* Persistent chat history using JSON
* Automatic history loading on startup
* Clear chat history command
* Timestamp for every conversation
* Improved project structure and code organization

## Author

**Donya Hamidi**
