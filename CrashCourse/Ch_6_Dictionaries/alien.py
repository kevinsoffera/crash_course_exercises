alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# new_points = alien_0['points']
# print(f"You just got {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"Original position: {alien_0['x_position']}")

# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")


alien_0['speed'] = 'medium'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# THe new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Use 'del' to delete a key-value pair, permanently
del alien_0['points']
print(alien_0)

