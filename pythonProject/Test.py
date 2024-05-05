import time


def math():
    question1 = float(input("Give me one number.\n"))
    question2 = float(input("Give me another number.\n"))
    symbol = input("Give me a symbol. EX: +/-*\n")

    if symbol == "+":
        print(question1 + question2)
        time.sleep(1)
        intro()

    elif symbol == "/":
        print(question1 / question2)
        time.sleep(1)
        intro()

    elif symbol == "-":
        print(question1 - question2)
        time.sleep(1)
        intro()

    elif symbol == "*":
        print(question1 * question2)
        time.sleep(1)
        intro()

    else:
        print("Did not understand, restarting.")
        time.sleep(1)
        math()


def intro():
    name = input("Hello! I am a new chatbot, what is your name?\n")
    answer = input("Hello, " + name + "! I have a math feature, a simple chat feature.  Which one?\n")

    if answer == "MT":
        math()

    elif answer == "SC":
        second_question = input("1: Math, 2: Life.")
        if second_question == "1":
            print("I'll run calculator.")
            math()


intro()
