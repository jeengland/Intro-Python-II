import textwrap


# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def lookForItems(self):
        if not self.items:
            print('There\'s nothing here.')
        else:
            print('You can see the following items:')
            for item in self.items:
                print(item)
