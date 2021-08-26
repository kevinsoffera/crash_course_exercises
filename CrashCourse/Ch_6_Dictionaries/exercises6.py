# 6.1 Person
# person = {'first_name': 'kevin', 'last_name': 'soffera', 'city': 'collegeville'}
# print(person['first_name'].title(), person['last_name'].title(), 
#       person['city'].title())
# #  or
# print(f"First name: {person['first_name'].title()}")
# print(f"Last name: {person['last_name'].title()}")
# print(f"City: {person['city'].title()}")


# 6.2 Favorite Numbers
#   failure: tried to make the print output neat using a for loop - 
#            didn't know how to grab one key-value pair at a time

# favorite_numbers = {
#     'kevin': '98', 
#     'jondz': '156', 
#     'porkiln': '54',
#     'aerth': '2',
#     'boviser': '63'
#     }

# print(favorite_numbers)

# 6.3 Glossary
# glossary = {
#     'get': 'method to set a default value that will be returned if the key '
#            'does not exist',
#     'tuple': 'an immutable list, denoted using ()',
#     'dictionary': 'a list of key-value pairs, denoted using {}',
#     'variable': 'defined value',
#     'pep': 'python enhancement proposal',
#     'set': 'a collection in which each item must be unique',
#     'boolean expression': 'a conditional test',
#     'pop': ' a method to delete the last element in a list',
#     'loop': 'a method of repeating the same action or actions',
#     'sort': 'a method to sort a list or other collection',
# }
# print(f"get:  {glossary['get']}")
# print(f"\ntuple: {glossary['tuple']}")
# print(f"\ndictionary: {glossary['dictionary']}")
# print(f"\nvariable: {glossary['variable']}")
# print(f"\npep: {glossary['pep']}")

# # 6.4 Glossary 2
# for word, definition in glossary.items():
#     print(f"\nWord: {word}. Definition: {definition}")

# 6.5 Rivers
# rivers = {'thames': 'england', 'nile': 'egypt', 'yellow': 'china'}
# for river, country in rivers.items():
#     print(f"The {river.title()} river runs through {country.title()}.")
# for river in rivers:
#     print(river)
# for country in rivers.values():
#     print(country)

# 6.6 Polling
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# should_take_poll_names = ['edward', 'drondo', 'lokapo', 'jen', 'utria']
# for name in should_take_poll_names:
#     if name in favorite_languages.keys():
#         print(f"Thank you for taking the poll, {name.title()}!")
#     else:
#         print(f"{name.title()}, please take the poll!")


# 6.7 People
# person_0 = {'first': 'kevin', 
#             'last': 'soffera', 
#             'city': 'collegeville',
# }
# person_1 = {'first': 'jontry',
#             'last': 'tilopin',
#             'city': 'viyaber',
# }
# person_2 = {'first': 'ellabee',
#             'last': 'smisch',
#             'city': 'larvantree',    
# }
# people = [person_0, person_1, person_2]
# for person in people:
#     full_name = f"{person['first']} {person['last']}"
#     location = person['city']
#     print(f"\nFull name: {full_name.title()}")
#     print(f'Home town: {location.title()}')

# 6.8 Pets
# pet_0 = {'animal': 'dog',
#          'name': 'lonkug',
#          'owner': 'partisious',
# }
# pet_1 = {'animal': 'parrot',
#          'name': 'ilkaloi',
#          'owner': 'malklypso',
# }
# pet_2 = {'animal': 'cat',
#          'name': 'puire',
#          'owner': 'chandry'
# }
# pets = [pet_0, pet_1, pet_2]
# for pet in pets:
#     print(f"\nAnimal: {pet['animal'].title()}")
#     print(f"Name: {pet['name'].title()}")
#     print(f"Owner's name: {pet['owner'].title()}")

# 6.9 Favorite Places
# favorite_places = {'trinks': ['italy', 'moscow'],
#                    'klinver': ['warsaw'],
#                    'rethune': ['fiji', 'jakarta', 'laos']    
# }
# for person, places in favorite_places.items():
#     print(f"\nName: {person.title()}'s favorite places are:")
#     for place in places:
#         print(f'\t{place.title()}')

# 6.10 Favorite Numbers (taken from 6.2)
# favorite_numbers = {
#     'kevin': ['95', '436'], 
#     'jondz': ['156', '367', '817'], 
#     'porkiln': ['54', '2156', '65', '90'],
#     'aerth': ['2', '542', '764', '9018763'],
#     'boviser': ['63'],
# }
# for person, numbers in favorite_numbers.items():
#     print(f"{person.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f'\t{number}')

# 6.11 Cities
# cities = {
#     'Philadelphia': {
#         'country': 'america',
#         'population': '1.579 million',
#         'fact': 'known as the "City of Brotherly Love',
#     },
#     'Tokyo': {
#         'country': 'japan',
#         'population': '13.96 million',
#         'fact': 'originally a fishing village named "Edo"',
#     },
#     'Rome': {
#         'country': 'italy',
#         'population': '2.873 million',
#         'fact': 'Rome is also known as "Caput Mundi"',
#     },
# }
# for city, city_info in cities.items():
#     print(f"\nCity: {city.title()}")
#     print(f"\tCountry: {city_info['country'].title()}")
#     print(f"\tPopulation: {city_info['population']} people.")
#     print(f"\tFun little fact: {city_info['fact']}")

# 6.12 Extensions
# Skipped this one, didn't think of any/want to do any improvements
# maybe come back to it for xtra practice



















