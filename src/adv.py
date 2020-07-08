import textwrap
import os
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before
    you, falling into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
    west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(room['outside'], "Player")
done = False
newRoom = True

availableCommands = [
    "help    - Bring up a list of commands",
    "quit    - Exit the game",
    "check   - Look around the current room",
    "n/s/e/w - Walk in the corresponding cardinal direction"
]


def printCommandList():
    for commandDescription in availableCommands:
        print(commandDescription)


c = {
    "red": "\033[31m",
    "yellow": "\033[93m",
    "end": "\033[0m"
}

os.system('cls' if os.name == 'nt' else 'clear')

while not done:
    if newRoom:
        player.printRoomDescription()
        newRoom = False
    cmd = input('>>> ')
    if cmd == 'q' or cmd == 'quit':
        done = True
    elif cmd == 'help':
        printCommandList()
    elif cmd == 'check':
        player.printRoomDescription()
    elif cmd == 'n' or cmd == 'e' or cmd == 's' or cmd == 'w':
        if player.movePlayer(cmd):
            newRoom = True
    else:
        print(f'{c["red"]}I can\'t do that!{c["end"]}')
