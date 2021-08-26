# 5.1 Conditional Tests

# car = 'subaru'
# # print("Is car == 'subaru'? I predict True.")
# # print(car == 'subaru')

# # print("\nIs car == 'audi'? I predict False.")
# # print(car == 'audi')

# fish = ['red', 'gills', 'neat', 'swims']
# print('red' in fish)
# print('lame' in fish)
# print(fish == 'cool')
# print(1 == 2)
# print(90870 != 490328740)


# # 5.2 More Conditional Tests

# color = 'Chartruese'
# print(color == 'Chartruese')
# print(color == 'red')

# print(color == 'chartruese')
# print(color.lower() == 'chartruese')

# print(1 == 1 or 1 == 2)
# print(10 > 5 and 10 <= 21)

# 5.3 Alien Colors # 1 and 5.4 Alien Colors # 2 and 5.5 Alien Colors # 3
# alien_color = 'green'

# if alien_color == 'green':
#     print("You just earned 5 points for murder!")
# if alien_color == 'red':
#     print("You just earned 10 points for murder!")

# if alien_color == 'green':
#     print("You just earned 5 points for murder!")
# else:
#     print("You just earned 10 points for murder!")

# if alien_color == 'green':
#     print("You just earned 5 points for murder!")
# elif alien_color == 'yellow':
#     print("You just earned 10 points for murder!")
# elif alien_color == 'red':
#     print("You just earned a whopping 15 points for murder!")

# 5.6 Stages of Life

# age = 22

# if age < 2:
#     print("You are a baby.")
# elif age < 4:
#     print("Toddler-lookin ass.")
# elif age < 13:
#     print("Literal child.")
# elif age < 20:
#     print("You're a teenager. Good luck lmao.")
# elif age < 65:
#     print("You're an adult and have increasingly cumbersome responsibilities.")
# elif age >= 65:
#     print("You are an elder.")


# 5.7 Favorite Fruit

# favorite_fruits = ['orange', 'raspberry', 'mango']
# if 'orange' in favorite_fruits:
#     print("Yeah I like oranges.")
# if 'banana' in favorite_fruits:
#     print("Yes I consume bananas.")
# if 'mango' in favorite_fruits:
#     print("Yep, I eat mango.")
# if 'raspberry' in favorite_fruits:
#     print("Mmmmm raspberry.")
# if 'apple' in favorite_fruits:
#     print("Crunch on apple for enjoyment.")

# 5.8 Hello Admin

# usernames = ['admin', 'ksoffera', 'chunkyman', 'stegos', 'manicpixiedreamgirl']

# for username in usernames:
#     if username == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {username}, thanks for logging on to Neopets.")

# 5.9 No Users

# usernames = []

# if usernames:
#     for username in usernames:
#         print(f"Hello {username}, welcome back.")
# else:
#     print("Uh oh, we need some users!!")

# 5.10 Checking usernames

# current_users = ['Kevin', 'chug', 'jimg', 'poai', 'charles']

# lower_current_users = []
# for current_user in current_users:
#     lower_current_users.append(current_user.lower())

# new_users = ['KEVIN', 'kial', 'poai', 'tuay', 'vico']

# for new_user in new_users:
#     if new_user.lower() in lower_current_users:
#         print(f"Sorry, '{new_user}' is taken, you gotta pick a different " 
#                "username dude.")
#     else:
#         print(f"{new_user} is available!")


# 5.11 Ordinal Numbers
ordinal = range(1,10)
for number in ordinal:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")












