# -*- coding: utf-8 -*-
from sys import exit

# Global inventory
# if you hold the two items then magic the key for the north door.
inventory = []

def start():
    # it was a dark and stormy night.
    print """
    It was dark and stormy night.
    A cave of wonder lies before you.
    The wind whispers into your ear.
    -- Welcome traveller, to the cave of bullshit.
    -- To reach the treasure to the north you must restore the Wand of Magic to its former glory.
    -- Look to the west for the Stone of Rocks.
    -- And to the east for the Stick of Wood.
    -- Go now, and fulfill the prophecy.
    -- ...
    -- And take care.
    -- Mwahahaha.

    The voice leaves you and you press forward into the cave.
    Now, where to from here...

    """
    userInput = raw_input("> ")

    if "west" in userInput:
        #go west
        west()
    elif "east" in userInput:
        #go east
        east()
    elif "north" in userInput:
        # go north, check for items
        north()
    else:
        # try again
        start()
    return

def dead(mortalCoil):
    # This is what it says when you die.
    print mortalCoil, ", Good job!"
    exit(0)

def returnToStart():
    # Second or more vised to hub, skip all dialog.
    print """

    ---------------

    You clamber back to the entrance of the cave.
    'east, west or north?' farted the wind...
    """

    userInput = raw_input("> ")

    if "west" in userInput:
        #go west
        west()
    elif "east" in userInput:
        #go east
        east()
    elif "north" in userInput:
        # go north, check for items
        north()
    else:
        # try again
        returnToStart()
    return

def west():
    print """
    You press on wesht, feeling that this is the besht thing to do.
    Some pure mad fella jumps out before you, spewing cliché's.
    His rawwness makes your toes curl.

    -- See you boyo, I have this rock here that that the wind tell's me you fancy.
    -- I'm not here to judge boss, just to ask you the riddle.
    ---'
    --- Many have heard me,
    --- but no one has seen me,
    --- and I will not speak back
    --- until spoken to.
    ---
    --- Who am I?
    ---'
    -- What do ya make of that now?
    -- You can have as many goes as you like as long as you dont use the 'f' word.
    """
    def westRiddle():

        # travel west into the cave. Find the magic rock.
        userInput = raw_input("> ")

        if "echo" in userInput:
            print """
            -- The brains on this buck!
            -- Well now, the stone is yours.
            -- Go over yonder and pick it up from the pile of important rocks.

            ...

            ...

            *Stone of Rocks added to inventory*

            """
            --

            inventory.append("Stone")

            returnToStart()

        elif "fuck" in userInput:
            dead("The oul fella trampled ya for cursin.")
        else:
            print "Have another go."
            westRiddle()

        return

    westRiddle()
    return

def east():
    # travel east into the cave. Find the magic stick.
    print """
    ~ Woe on to you, grand fucker, who seeks the Stick of Wood.~

    The voice seemed to come from inside your own brain.

    ~ A heavy price you must pay before this most holy relic can be yours ~

    * Before you, a change cup appears *

    You feel a rattle in your pocket.

    You have quids upon quids!

    ~ Now, what do you think is a reasonable price for such a fine relic ~

    ...

    How many quid do you throw in the fucking cup?

    """

    def quidSpammer():

        userInput = raw_input("> ")

        if isinstance(userInput, (int,long)) == True:
            print "You idiot, thats not a number of quid!"
            print "Try again!"
            quidSpammer()

        elif userInput < 10:
            print "You stingy fucker!"
            dead("The voice in your head drowns you in quids.")

        else:
            print "You prince!"
            print """
            You win!

            ...

            ...

            *Stick of Wood added to inventory*

            """

            inventory.append("Stick")

            returnToStart()


    quidSpammer()

    return

def north():
    print """
    Do you want to bring forth the wand of wands?
    ..
    ..
    Yes or No?
    """
    def doorTalker():
        userInput = raw_input("> ")
        if "Yes" in userInput:
            checkIfWorthy()
        elif "No" in userInput:
            returnToStart()
        else:
            print "That's not an answer...."
            doorTalker()

    doorTalker()

    return
    #travel north into the cave. You need the magic wand.

def checkIfWorthy():
    # Check if you have both parts of the wand in your inv.
    if "Stone" and "Stick" in inventory:
        print "You bring forth the Wand of Wands and blow the shit out of the door."
        print "You take all the loot you can carry"
        print "Congrats!"

    else:
        dead("Dont be going to try that now sonney, you dead now.")
    return



start()
