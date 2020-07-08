import textwrap

c = {
    "red": "\033[31m",
    "yellow": "\033[93m",
    "end": "\033[0m"
}


# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self.items = []

    def printRoomDescription(self):
        room = self.location
        title = [f'{c["yellow"]}--- {room.name} ---{c["end"]}']
        description = title + textwrap.wrap(' '.join(room.description.split()))
        for line in description:
            print(line)

    def movePlayer(self, direction):
        currentRoom = self.location
        move = f'{direction}_to'
        if hasattr(currentRoom, move):
            self.location = getattr(currentRoom, move)
            return True
        else:
            print('There is no room in that direction.')
            return False

    def checkInventory(self):
        if len(self.items) == 0:
            print('I\'m not holding anything!')
        else:
            print('I\'m holding the following items:')
            for item in self.items:
                print(item)
