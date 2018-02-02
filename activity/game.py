#! /usr/bin/python3

# This will be a functional programming exercise. No classes or objects just
# yet. Linear path (mainly) only.

end = False
reaper = True
staff = False
riddle = False
charge = False
TTT_door = "closed"
Ana_door = "closed"
room = "start"

while end != True:
    if room = "start":
        print('You find yourself in a room. There is a door at the end.')
        print('What do you want to do?')
        print('Actions available: look at door, forward, look around')
        user_in = input('> ')
        if user_in = "look at door":
            if TTT_door = "closed":
                print('You look at the door')
                # logic for solving the door here
            else:
                print('The door is open. You cannot see into the room beyond.')
                print('What do you want to do?')
                print('Actions available: look at door, forward, look around')
        else if user_in = "forward":
            room = "one"
        else if user_in = "look around":
            # text about looking around
            # ask about staff
        else:
            print('That\'s not a valid entry. Try again.')
            user_in = input('> ')
    else if room = "one":
        # riddle and look around
    else if room = "two":
        # show door if they look; add sound of reaper if alive
    else if room = "three":
        # reaper if alive, dead reaper if not
        if reaper = True & & staff = False | | charged = False:
            # sad ending
            end = True
            # break out
    else:
        # Happy ending
        end = True
        # break out
