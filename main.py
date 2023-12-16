#FOR MacOS
# import os
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1")
#     x = input("Enter what you want to pronounce: ")
#     command = f"say {x}"
#     os.system(command)

import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1")
    while True:
        x = input("Enter what you want to pronounce: ")
        if x == 'q':
            engine.say("Bye Bye Friend")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
