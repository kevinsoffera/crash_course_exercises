from car import Car

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

# Modifying an attribute's value directly
# my_new_car.odometer_reading = 23

# Modifying an attribute's value through a method (see update_odometer above)
my_new_car.update_odometer(24)
my_new_car.read_odometer()
# Incrementing an attribute's value through a method(see increment_odometer)
my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()