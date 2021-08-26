def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# The asterisk in the parameter name *toppings tells Python to make
#  an empty tuple called toppings and pack whatever values it receives
#  into this tuple.
# Arbitrary parameters like *toppings must be collected last
# Will often see the generic parameter name *args, which collects arbitrary
#  positional arguments like this


