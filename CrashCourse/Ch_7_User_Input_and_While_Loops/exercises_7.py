# 7.1 Rental Car
# car = input("What kind of rental car would you like? ")
# print(f"\nOk, let me see if I can find a {car} for you.")

# 7.2 Restaurant Seating
# party = input("How many people are in your party? ")
# party = int(party)
# if party > 8:
#     print("\nSorry, you have too many friends and will have to wait for a table.")
# else:
#     print("\nRight this way, folks.")

# 7.3 Multiples of Ten
# number = int(input("Hey kid, gimme a random number: "))

# if number % 10 == 0:
#     print(f"\nEy whaddya know, {number} is a multiple of ten kiddo!")
# else:
#     print(f"\nSorry bucko, {number} ain't no multiple of ten.")

# 7.4 Pizza Toppings
# prompt = "\nWhat do you want on your pizza?"
# prompt += "\n(Enter 'quit' when you're done.) "

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else:
#         print(f"Adding {topping} to your pizza.")


# 7.5 Movie Tickets
# prompt = "\nEnter your age to see your movie ticket price."
# prompt += "\n(Enter 'quit' to stop.) "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     elif int(age) < 3:
#         print("Your ticket is free!")
#     elif int(age) >= 3 and int(age) <= 12:
#         print("Your ticket is $10.")
#     elif int(age) > 12:
#         print("Your ticket is $15.")

# 7.6 Three Exits - skipped. 

# 7.7 Infinity
# truth_reached = False
# while truth_reached == False:
#     print("Wha?")

# 7.8 Deli 
# sandwich_orders = ['italian', 'meatball', 'grilled cheese', 'pb&j',
#                     'ham', 'egg salad']
# finished_sandwiches = []

# while sandwich_orders:
#     finished_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(finished_sandwich.title())
# print(finished_sandwiches)

# 7.9 No Pastrami
# sandwich_orders = ['italian', 'meatball', 'pastrami', 'grilled cheese', 'pb&j',
#                     'ham', 'pastrami', 'egg salad', 'pastrami']
# finished_sandwiches = []

# print("The deli has run out of pastrami.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     finished_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(finished_sandwich.title())
# print(finished_sandwiches)

# 7.10 Dream Vacation
# responses = {}

# # Flag to indicate active polling
# polling_active = True

# while polling_active:
#     # Prompt for user input - name and response
#     name = input("\nWhat is your name? ")
#     response = input("What is your dream vacation? ")

#     # Store in dictionary
#     responses[name] = response

#     # See if more people are taking the poll
#     repeat = input("Is someone else going to respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# # Polling complete. Show results
# print("\n_-_ Poll Results _-_")
# for name, response in responses.items():
#     print(f"{name.title()}'s dream vacation is {response}!")



