filename = 'guest.txt'

new_guest = input("Please enter your name: ")

with open(filename, 'a') as file_object:
    file_object.write(f"{new_guest} \n")



