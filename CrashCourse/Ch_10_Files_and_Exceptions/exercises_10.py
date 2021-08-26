# 10.1 Learning Python
# filename = 'learning_python.txt'

# with open(filename) as file_object:
#     contents = file_object.read()
# # Print entire file
# print(contents)
# # Print by looping over file object
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
# # Print by storing lines in list, working with them outside with statement
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.strip())

# 10.2 Learning C
# with open(filename) as file_object:
#     contents = file_object.read()

# print(contents.replace('Python', 'C'))

# 10.3 Guest - also in guest.py, writes to guest.txt
# filename = 'guest.txt'

# new_guest = input("Please enter your name: ")

# with open(filename, 'a') as file_object:
#     file_object.write(f"{new_guest} \n")

# 10.4 Guest Book - writes to guest_book.txt
# filename = 'guest_book.txt'

# while True:
#     new_guest = input("Please enter your name. Enter 'quit' to quit: ")
#     if new_guest == 'quit':
#         break
#     else:
#         print(f"Welcome to the shin-dig, {new_guest}!")
#         with open(filename, 'a') as file_object:
#             file_object.write(f"{new_guest} \n")

# 10.5 Programming Poll - writes to poll_results.txt
# filename = 'poll_results.txt'

# while True:
#     response = input('Why do you like programming? \nType "quit" to quit. ')
#     if response == 'quit':
#         break
#     else:
#         print("Thank you for your response.\n")
#         with open(filename, 'a') as file_object:
#             file_object.write(f'{response} \n')

# 10.6 Addition and 10.7 Addition Calculator (Adds the while loop)
# print("Give me two numbers, and I'll add them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nEnter the first number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nEnter the second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("\nHey fuckwit, I said two numbers, not letters or symbols!")
#     else:
#         print(f"\nThe sum of the numbers is {answer}.")

# 10.8 Cats and Dogs & 10.9 Silent Cats and Dogs - see cats.txt and dogs.txt

# def read_file(filename):
#     """Display the text in a file"""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # print(f"Sorry, the file {filename} does not exist.")
        
#         pass
#     else:
#         print(f'{filename} says: \n{contents}\n')

# filenames = ['cats.txt', 'dogs.txt']
# for filename in filenames:
#     read_file(filename)

# 10.10 Common Words
# https://gutenberg.org/

# filename = 'don_quixote.txt'

# with open(filename, encoding = 'utf-8') as f:
#     contents = f.read()
# the_count = contents.count('the ')
# print(the_count)

# 10.11 Favorite Number
# import json

# fav_number = input("What is your favorite number? ")

# filename = 'fav_number.json'
# with open(filename, 'w') as f:
#     json.dump(fav_number, f)

# filename = 'fav_number.json'
# with open(filename) as f:
#     fav_number = json.load(f)

# print(f"I know your favorite number! It's {fav_number}!")


# 10.12 Favorite Number Remembered
# import json

# Load the favorite number, if it as been stored
#  If not, prompt for the number and store it

# filename = 'fav_number.json'

# try:
#     with open(filename) as f:
#         fav_number = json.load(f)
# except FileNotFoundError:
#     fav_number = input("What is your favorite number? ")
#     with open(filename, 'w') as f:
#         json.dump(fav_number, f)
#         print("I will remember this, flesh golem.")
# else:
#     print(f"Your favorite number is {fav_number}!") 

# 10.13 Verify User - see remember_me.py
# Added verification steps - may be inefficient, review at some point?

