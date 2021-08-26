motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

