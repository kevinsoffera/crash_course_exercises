favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# A set is a collection in which each item must be unique.
# A set allows for us to not have repeated values in this example
# Sets are built as follows = {'a', 'b', 'c'}
# Sets have {} but do not have a pair associated with them

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
