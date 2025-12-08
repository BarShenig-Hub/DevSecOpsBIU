# This script implements a simple command-line interface (CLI) loop.
user_input = input("mycli> ")

while user_input != "quit":
    if user_input != "":
        print(user_input, "is a nice command")
        user_input = input("mycli> ")
    else:
        user_input = input("mycli> ")

print("Got quit command, goodbye.")