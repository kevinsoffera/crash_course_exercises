def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert', 'einstein',
#                             location= 'princeton',
#                             field= 'physics')
# print(user_profile)

# The double asterisks before the paramter **user_info cause Python to create
#  an empty dictionary called user_info and pack whatever name-value pairs
#  it receives into this dictionary.
# Will often see the parameter name **kwargs used to collect non-specific
#  keyword arguments.
