# 8.1 Message
# def display_message():
#     """Display what I am learning this chapter"""
#     print("In this chapter, I am learning all about functions.")
# display_message()

# 8.2 Favorite Book
# def favorite_book(title):
#     """Display message about a favorite book"""
#     print(f"One of my favorite books is {title.title()}.")
# favorite_book('the very hungry caterpillar')

# 8.3 T-Shirt
# def make_shirt(size, message_text):
#     """Display shirt size and shirt message """
#     print(f'The shirt is a size {size} and reads: "{message_text}".')
# make_shirt('medium', 'please do not speak to me')
# make_shirt(size='medium', message_text='please do not speak to me')

# 8.4 Large Shirts
# def make_shirt(size='large', message_text='I love Python'):
#     """Display shirt size and shirt message """
#     print(f'The shirt is a size {size} and reads: "{message_text}".')
# make_shirt()
# make_shirt(size='medium')
# make_shirt(size='half-medium', message_text='orange juice and toothpaste')

# 8.5 Cities
# def describe_city(city,country='Japan'):
#     """Display a city and its country"""
#     print(f"{city.title()} is in {country}.")
# describe_city('tokyo')
# describe_city('kyoto')
# describe_city(city='warsaw')

# 8.6 City Names
# def city_country(city, country):
#     """Display a city and its country"""
#     formatted_city = (f"{city.title()}, {country.title()}")
#     print(formatted_city)

# city_country('rome', 'italy')
# city_country('tokyo', 'japan')
# city_country('oslo', 'norway')

# 8.7 Album
# def make_album(artist_name, album_title, number=None):
#     """Display dictionary of an artist's name and their album title"""
#     name_title = {'name': artist_name, 'album': album_title}
#     if number:
#         name_title['number'] = number
#     return name_title

# musician = make_album('freddie gibbs', 'alfredo')
# print(musician)
# musician1 = make_album('earl sweatshirt', 'some rap songs',number = 12)
# print(musician1)
# musician2 = make_album('black thought', 'streams of thought')
# print(musician2)

# 8.8 User Albums
# while True:
#     print("\nPlease enter your favorite musician and their album: ")
#     print("(enter 'q' at any time to quit.)")

#     artist = input("Artist's name: ")
#     if artist == 'q':
#         break

#     album = input("One of their albums: ")
#     if album == 'q':
#         break
#     print(make_album(artist, album))


# 8.9 Messages
# messages = ['hello',
#             'poggers',
#             'what is up jimbo',
#             'video games'
            # ]

# def show_messages(messages):
    # """Display what message is being read"""
#     for message in messages:
#         print(message)
# show_messages(messages)

# 8.10 Sending Messages
# def send_messages(messages, sent_messages):
#     """
#     Display what message is being read
#     Move each message to sent messages
#     """
#     while messages:
#         current_message = messages.pop()
#         print(f"Current Message: '{current_message}'")
#         sent_messages.append(current_message)
        
# sent_messages = []
# send_messages(messages)
# print(messages)
# print(sent_messages)

# 8.11 Archived Messages
# send_messages(messages[:], sent_messages)
# print(messages)
# print(sent_messages)

# 8.12 Sandwiches
# def make_sandwich(*ingredients):
#     """Display a message about the sandwich being made"""
#     print(f"Making a sandwich with:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")
# make_sandwich('lettuce')
# make_sandwich('lettuce', 'cheese')
# make_sandwich('lettuce', 'cheese', 'bread', 'ham')

# 8.13 User Profile
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# kevin_profile = build_profile('kevin', 'soffera', hair='brown', meat='huge',
#                             job='geologist')
# print(kevin_profile)

# 8.14 Cars
# def make_car(manufacturer, model_name, **car_profile):
#     """Build a dictionary about a car"""
#     car_profile['manufacturer'] = manufacturer
#     car_profile['model_name'] = model_name
#     return car_profile

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# 8.15 Printing models
# see printing_functions.py

# 8.16 Imports
# import user_profile
# from user_profile import build_profile
# from user_profile import build_profile as bp 
# import user_profile as up 
# from user_profile import *

# 8.17 Styling Functions