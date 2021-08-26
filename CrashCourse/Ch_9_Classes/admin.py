"""A set of classes to summarize admin info and privileges."""
from user import User

class Admin(User):
    """Summarize information about an administrator."""

    def __init__(self, first_name, last_name, location, ele_type):
        super().__init__(first_name, last_name, location, ele_type)
        self.privileges = Privileges()

    
# my_admin = Admin('kevin', 'soffera', 'collegeville', 'fire')
# my_admin.show_privileges()

class Privileges:
    def __init__(self):
        """Simple summary of admin privileges."""
        self.privileges = ['can add post', "can delete post", "can ban user",
                           'can warp space-time']

    def show_privileges(self):
        """Display a message about the privileges of an admin"""
        print(f"The Admin can: ")
        for privilege in self.privileges:
            print(privilege)

# my_new_admin = Admin('yortie', 'trevalex', 'new york', 'space')
# my_new_admin.privileges.show_privileges()