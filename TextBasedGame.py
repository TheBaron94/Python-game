# Adam Schmidt
# Wendigo The Game
# Last updated 4/17/2021

room_current = 'Adams Bedroom'  # Set starting global variable
inventory = []  # Set starting global
# Define rooms and options.
rooms = {
        'Adams Bedroom': {'South': 'Stairs'},
        'Stairs': {'North': 'Adams Bedroom', 'East': 'Living Room', 'South': 'Moms Office'},
        'Moms Office': {'North': 'Stairs'},
        'Living Room': {'North': 'Garage', 'East': 'Kitchen', 'South': 'Utility Room', 'West': 'Stairs'},
        'Garage': {'South': 'Living Room'},
        'Utility Room': {'North': 'Living Room'},
        'Kitchen': {'East': 'Porch', 'South': 'Kitchen Pantry'},
        'Porch': {'West': 'Kitchen'},
        'Kitchen Pantry': {'North': 'Kitchen'}
    }

# Define rooms and items in them.
items = {
    'Adams Bedroom': 'No item',
    'Stairs': 'No item',
    'Moms Office': 'Book of Native American Lore',
    'Living Room': 'Silver candle stick',
    'Garage': 'Silver Headed Axe',
    'Utility Room': 'Gas Can',
    'Kitchen': 'Box of salt',
    'Kitchen Pantry': 'Matches',
    'Porch': 'No item'
}


def intro():  # Background story to the game
    print(
        'Your name is Adam Schmidt, you live in northern Minnesota.\n'
        'You have been hearing some strange stories from your neighbours in the area.\n'
        'Stories about an ancient evil in the area, something called a \'Wendigo\'\n'
        'According to your friends the \'Wendigo\' used to be a human\n'
        'until it was forced to eat the flesh of others to survive.\n'
        'The monster has been in hibernation for years, but the rumors say it has awoken to feed again....\n'
        'Not that you believe in any of that crap.....\n'
        'Until tonight that is.\n'
        'Press Enter to continue:\n'
    )
    input()
    print()
    print()
    print(
        'Its well after midnight, and you have been asleep for awhile at this point\n'
        'You awaken to the sound of your mother softly knocking on your bedroom door\n'
        'You slowly get out of bed and open your door to let your mother in\n'
        '\'Adam I think some one is outside, I can hear them moving around my bedroom windows\'\n'
        '\'Probably just some dam junkie\' you think to yourself\n'
        'The area you and your mom live in isnt exactly a bad area,'
        'there just seems to be a fair amount of drug problems\n'
        'and it isnt all that uncommon for people to break into garages in the night looking for things to sell\n'
        'Press Enter to continue:\n'
    )
    input()
    print()
    print()
    print(
        'As you go to move past your mom,'
        'you can hear the distinct sound of glass shattering from what sounds like the porch\n'
        'Both you and your mom grow deathly still as you hear the sounds of foot steps on broken glass\n'
        'Suddenly a terrible stink fills your nose'
        'as the wind from out side carries the smell of whoever is now in your home up the stairs\n'
        'From downstairs you hear your mother call to you \'Adam can you come here please?\'\n'
        'But that cant be your mother.... She is crouching right next to you...\n'
        'And all at once a realization dawns on you, you know what that smell is, its the smell of rotting death\n'
        'You know now who is in your home, its not a junkie......\n'
        '...... it\'s the Wendigo\n'
        'Press Enter to continue:\n'
    )
    input()
    print()
    print()
    print(
        'You suddenly wish you had listened more to the locals stories about this monster\n'
        'Your only hope is to get the book about native american folk lore from your moms office\n'
        'and pray it holds some information about the Wendigo\n'
    )
    print()
    print('Instructions:\n'
          'In any of the rooms you will be given a list of possible directions and any items in the room\n'
          'To move in any direction simply type in the direction you would like to go and hit Enter\n'
          'To pickup an item type in \'Get\' and hit Enter\n'
          )
    print()
    input('Press Enter to start the game:')
    gameloop()


# Main game play loop
def gameloop():
    global room_current
    global inventory
    print()
    print()
    print('You are in {room}'.format(room=room_current))
    if room_current == 'Porch':  # trigger endgame if current room is porch
        endgame()
    options = rooms[room_current].items()
    direction_options = rooms[room_current].keys()
    for directions, room in options:  # List directions and rooms
        print('You can go {directions} to {room}'.format(directions=directions, room=room))
    item = items[room_current]  # Get item for this room based on room_current global var.
    print('This room contains: {}'.format(item))
    print('Your inventory: {}'.format(inventory))  # list current inventory.
    direction = input('What would you like to do?:\n').capitalize()  # get input from player
    if direction == 'Get':
        if item == 'No item':
            print('This room contains no item')
            input('Press Enter to continue')
            gameloop()
        else:
            inventory.append(item)  # add item to inventory
            items.update({room_current: 'No item'})  # Remove the item from the listing for this room.
            if item == 'Book of Native American Lore':  # this will run only if this is first time player gets book
                print()
                print('You grab the book from your mothers book shelf.\n'
                      'Flipping to the index you thankfully find a listing for Wendigo.\n'
                      'Turning quickly to the page you scroll to the bottom and find written there:\n'
                      '\'In order to kill a Wendigo one must:\n'
                      '1) Draw a protective circle around ones self in salt\n'
                      '2) Stab a silver object through the heart\n'
                      '3) Remove the head with silver axe\n'
                      '4) Destroy the head (Fire is recommended for this step)\n'
                      '\"Well I think we should have everything needed for this around the house\"\n'
                      'You think to yourself, \"I just have to make sure I get everything I need\n'
                      'before I go to the porch and try to kill this thing\"\n'
                      )
                input('Press Enter to continue')
            gameloop()
    elif direction in direction_options:
        room_current = rooms[room_current].get(direction)  # Update current room based on direction.
        gameloop()
    else:
        print('There is no room in that direction, or you have entered an invalid option')
        input('Press Enter to continue')
        gameloop()


# Endgame, triggered when player enters porch area.
def endgame():
    inventory_len = len(inventory)
    if inventory_len < 6:     # Test for all items in inventory
        print('As you move closer to the porch, you can hear the labored breathing of the monster\n'
              'You can smell the rotting flesh of its body\n'
              'You look down at what you\'re holding\n'
              '\"Oh god, I don\'t have everything I need\" you think to yourself\n'
              'As the beast suddenly turns its terrible animal like head in your direction\n'
              '.....It has picked up your scent\n'
              '\"Ahh there you are Adam\" it says in your mothers voice\n'
              'As it lunges towards you\n'
              '...\n'
              '...\n'
              '...\n'
              'Game over. You failed!\n'
              )
        print()
        try_again = input('Would you like to try again?: Yes or No\n').capitalize()
        if try_again == 'No':
            quit()
        elif try_again == 'Yes':
            reset()
    elif inventory_len == 6:
        print('You did it, you gathered all the items you need, now its time to end this\n'
              'You start by drawing a protective symbol in salt around your feet from the book,\n'
              'Next you swing the door to the porch wide open\n'
              'You can see the monster standing there, suddenly it turns its terrible animal like head towards you\n'
              '\"Ahh there you are Adam\" it says in your mothers voice\n'
              'As it lunges towards you\n'
              'You hold the Candle stick firm in your hand and jam it into the monsters chest as it falls on you\n'
              'It lets out a terrible howl of pain and falls twitching to the floor\n'
              '\"This is really going to suck\" you think to yourself as you ready the axe\n'
              'In one terrible chop you remove the monsters head\n'
              'Gingerly you pickup it up and carry it onto the lawn and set it ablaze using the gas and matches\n'
              '\"What a way to start the day\"\n'
              'Game over! You have Defeated the Wendigo!\n'
              )
        print()
        try_again = input('Would you like to play again?: Yes or No?\n').capitalize()
        if try_again == 'No':
            quit()
        elif try_again == 'Yes':
            reset()


# reset game variables and start over.
def reset():
    global room_current
    room_current = 'Adams Bedroom'
    global items
    items = {
        'Adams Bedroom': 'No item',
        'Stairs': 'No item',
        'Moms Office': 'Book of Native American Lore',
        'Living Room': 'Silver candle stick',
        'Garage': 'Silver Headed Axe',
        'Utility Room': 'Gas Can',
        'Kitchen': 'Box of salt',
        'Kitchen Pantry': 'Matches',
        'Porch': 'No item'
    }
    global inventory
    inventory = []
    print()
    print()
    intro()


# Main code.
intro()
