#! /usr/bin/python3
# initialise the game
room = "start"
monster_dead = False
sword = False
end = False
print('The Dark Tunnel')
# Loop while the player is not in the end room and alive
while end != True:
    if room == 'start':
        print('You are standing at the entrance to a long tunnel.')
        # Noise for the monster...
        if monster_dead == False:
            print('You hear a low rumbling in the distance.')
        print('What action would you like to do?')
        print('Actions available: forward, look')
        action = input('> ')
        # Just moves forward
        if action == 'forward':
            room = 'middle'
        # Look around
        elif action == 'look':
            if sword == True:
                print('You look around in the darkness, but there is\n'
                      'nothing here.')
            else:
                sword_action = input('You look around in the darkness, and see\n'
                                     'something shiny.\n'
                                     'Would you like to examine it? (yes/no)\n'
                                     '> ')
                if sword_action == 'yes':
                    getsword = input('It is a sword. Would you like to pick it\n'
                                     'up? (yes/no)?\n'
                                     '> ')
                    if getsword == 'yes':
                        print('You pick up the sword. Probably a good idea.')
                        sword = True
                    else:
                        print('You leave the sword in the dust. Is that\n'
                              'really a good idea?')
                else:
                    print('Not too curious, are you?')
            room = 'start'
        else:
            print('You cannot do that.')
            room = 'start'
    # The monster's room
    elif room == 'middle':
        if monster_dead == False:
            print('When you step forward, a monster leaps out at you with\n'
                  'fangs bright white and shining in the darkness!')
            if sword == True:
                print('You get really lucky, putting your sword up just in\n'
                      'time for the leaping monster to thrust its body upon\n'
                      'it. You kill the monster. Lucky bastard.')
                monster_dead = True
            else:
                print('You have no way to defend yourself! As the monster\n'
                      'crushes your chest, you have just enough time to regret\n'
                      'coming into this tunnel without some way to protect\n'
                      'yourself. Poor bastard. What were you thinking?\n'
                      'You are dead.\n'
                      'Game Over')
                end = True
        else:
            print("The monster's dead carcass lies on the floor, the sword\n"
                  "still embedded in its flesh.")
        # if the player is still alive, they can move
        if end != True:
            print("Actions available: forward, backward")
            cmd = input("> ")
            if cmd == 'forward':
                room = 'end'
            elif cmd == 'backward':
                room = 'start'
    # exit - win condition
    elif room == 'end':
        print('You made it past the monster and escaped the tunnel.\n'
              'Congratulations, you win!')
        end = True
