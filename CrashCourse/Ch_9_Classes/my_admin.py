from user import User
from admin import Admin, Privileges

my_admin = Admin('kevin', 'soffera', 'collegeville', 'golem')
my_admin.privileges.show_privileges()