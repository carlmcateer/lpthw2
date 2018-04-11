
import random
import time

# Design a game where you are in a boxing match with an AI
# It is a turn baed game where you have a fixed amount of stamina
# When stamina drops to zero it is the other players turn
#
# Both players have a life bar, when you life is 0 the game is over.
#
# You have 3 offencive moves ranging from low damage, low stamina, #reliable (jab)
# to high damage, high stamina, #unreliable (haymaker)
#
# Optional fetures:
#
# If you end your turn with stamina left over you have a chance to dodge attacks.
#
# In the opening menue you have the option to select more dificult chalanges(more live and stamina for enemy).
#
# You can use cheat codes to win the game.
#
# Cross and Haymaker must be "set up"

class Intro(object):
    # Description of the game and how you play.
    pass

class Moves(object):

    #moves = ['jab','cross','haymaker']

    def jab(self):
        pass
    #
    # def cross(self):
    #     pass
    #
    # def haymaker(self):
    #     pass

    def pass_turn(self):
        pass

class Boxer(object):
    def __init__(self, name = '', life = 0, stamina = 0):
        self.name = name
        self.life = life
        self.stamina = stamina

class Player(Boxer):

    def choose_player_move(self):
        print "Whatch wana do champ?"
        time.sleep(1)
        print ".."

        user_input = raw_input("(jab or pass?)")

        if "jab" in user_input:
            Moves.jab()
        elif "pass" in user_input:
            Moves.pass_turn()
        else:
            choose_player_move()

class Enemey(Boxer):
    # trash_talk = [
    # "Get ready for the pain sukka!",
    # "Oh here it comes!",
    # "kaaaaameeeeeehaaaaaameeeeeehaaaaAaaaAAaa!"
    # ]
    #
    # print Enemey.trash_talk[randint(0,len(trash_talk)-1)]

    def choose_enemy_move():

        enemy_input = randint(0,2)

        if enemy_input == 0:
            Moves.jab()
        elif enemy_input == 1:
            Moves.pass_turn()
        else:
            print "Me no no!"

class Engine(object):
    pass

# class roundTimer():
#     turn = randint(0,1)
#
#     if turn == 0:
#         Player()

def choose_name():

    wait_time = 2

    print "Whats your name kid?"

    user_input = raw_input("> ")

    print "%s? I hope you are tougher then you sound..." % user_input
    time.sleep(wait_time)
    print "Lets see who you are up agenst."
    time.sleep(wait_time)
    print ".."
    time.sleep(wait_time)

    return str(user_input)

def choose_enemey():
    wait_time = 2

    bad_guy_names = [
    "Mohammed Ali",
    "Floyd Mayweather Jr.",
    "Sugar Ray Robinson",
    "Mike Tyson",
    "Joe Louis",
    "Manny Pacquiao",
    "Joe Frazier",
    "Rocky Marciano",
    "Vasyl Lomachenko"
    ]

    chosen_name = bad_guy_names[random.randint(0,len(bad_guy_names)-1)]
    print "Well if it aint none other than %s" % chosen_name
    time.sleep(wait_time)
    #dificulty options

    return chosen_name

player_name = choose_name()
enemey_name = choose_enemey()

player = Player(name = player_name, life = 10, stamina = 10)
enemy = Enemey(name = ememy_name, life = 10, stamina = 10)

print player.name
print player.life
print player.stamina

print enemey.name
print enemey.life
print enemey.stamina
