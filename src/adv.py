import textwrap
import os
from room import Room
from player import Player
from item import Item

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

# Declare all items

item = {
    'key': Item("Key", """A wrought iron key. It has somewhat of a heft
    to it."""),
    'coins': Item("Coins", """A pile of coins, presumable left by whoever
    looted the treasure chamber.""")
}

# Put items in appropriate rooms

room['foyer'].items = [item['key']]
room['treasure'].items = [item['coins']]

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
    "help           - Bring up a list of commands",
    "quit           - Exit the game",
    "n/s/e/w        - Walk in the corresponding cardinal direction",
    "check          - Look around the current room",
    "search         - Search for items in the current room",
    "inventory      - See what items are in your inventory",
    "take [item]    - Pick up an item",
    "drop [item]    - Drop an item",
    "examine [item] - Examine an item"

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
    instructions = input('>>> ')
    cmd = instructions.split()[0].lower()
    obj = ''
    if len(instructions.split()) > 1:
        obj = instructions.split()[1].lower()
    if cmd == 'q' or cmd == 'quit':
        done = True
    elif cmd == 'help':
        printCommandList()
    elif cmd == 'check':
        player.printRoomDescription()
    elif cmd == 'n' or cmd == 'e' or cmd == 's' or cmd == 'w':
        if player.movePlayer(cmd):
            newRoom = True
    elif cmd == 'search':
        player.location.lookForItems()
    elif cmd == 'inventory':
        player.checkInventory()
    elif cmd == 'get' or cmd == 'take':
        if obj == '':
            print(f'{cmd.capitalize()} what?')
        else:
            if obj in item:
                room = player.location
                targetItem = item[obj]
                if targetItem in room.items:
                    room.items.remove(targetItem)
                    player.items = player.items + [targetItem]
                    targetItem.on_take()
                else:
                    print('I don\'t see anything like that.')
            else:
                print('I don\'t see anything like that.')
    elif cmd == 'drop':
        if obj == '':
            print('Drop what?')
        else:
            if obj in item:
                room = player.location
                targetItem = item[obj]
                if targetItem in player.items:
                    player.items.remove(targetItem)
                    room.items = room.items + [targetItem]
                    targetItem.on_drop()
                else:
                    print('I don\'t have that.')
            else:
                print('I don\'t have anything like that.')
    elif cmd == 'examine':
        if obj == '':
            print('Examine what?')
        else:
            if obj in item:
                room = player.location
                targetItem = item[obj]
                if targetItem in player.items:
                    targetItem.on_examine()
                elif targetItem in room.items:
                    targetItem.on_examine()
                else:
                    print('I don\'t see anything like that.')
            else:
                print('I don\'t see anything like that.')
    else:
        print(f'{c["red"]}I can\'t do that!{c["end"]}')
