import textwrap


# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name

    def printRoomDescription(self):
        room = self.location
        title = '--- {name} ---'.format(name=room.name)
        description = [title] + textwrap.wrap(room.description)
        for line in description:
            print(line)

    def setRoom(self, room):
        self.location = room
