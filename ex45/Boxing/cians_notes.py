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

import random
import time

wait_time = 1.5

# Im not sure if it makes sence for this to be a class as ther is no INIT
class Moves(object):

    # Each move checks the users stamina before the move is attempted.
    # If the usere has enough stamina then the miss chance will determin if it is sucscsfull
    # Look up static method
    # array is miss chance, stamina cost and damage

    attack = {
    'jab': [1, 2, random.randint(1, 3)],
    'cross': [5, 4, random.randint(3, 5)],
    'haymaker': [9, 10, random.randint(7, 10)]
    }

    punch_line = [
    "%s lands a beutiful strike!",
    "A wopper landed stright down the pipe by %s",
    "I cant believe it! %s lands!!!!"
    ]

    miss_line = [
    "%s can't find his range!",
    "Ohh %s does not connect!",
    "Swing and a miss for %s!"
    ]

    def punch(self, move, user, target):
        miss_chance = Moves.attack.get(move)[0]
        stamina_cost = Moves.attack.get(move)[1]
        damage = Moves.attack.get(move)[2]

        if user.stamina >= stamina_cost:
            if miss_chance < random.randint(1, 10):
                user.stamina = user.stamina - stamina_cost
                target.life = target.life - damage
                time.sleep(wait_time)
                print Moves.punch_line[random.randint(0,2)] % user.name
                print "%s stamina: " % user.name + str(user.stamina)
                print "%s life: " % target.name + str(target.life)
                time.sleep(wait_time)
            else:
                user.stamina = user.stamina - stamina_cost
                time.sleep(wait_time)
                print Moves.miss_line[random.randint(0,2)] % user.name
                print "%s stamina: " % user.name + str(user.stamina)
                print "%s life: " % target.name + str(target.life)
                time.sleep(wait_time)
        else:
            print "Not enough stamina!"


# The user and the computer are the instances of the same class,
# The two core values are life and stamina,
# It costs stamina to atempt a move, and if it is sucsesfull then it will
# remove life points from the opponant
class Boxer(object):

    def __init__(self, name='', life=0, stamina=0):
        self.name = name
        self.life = life
        self.stamina = stamina

# Takes the users name so its can be used later in dialog
def choose_name():

    print "Whats your name kid?"

    user_input = raw_input("> ")

    print "%s? I hope you are tougher then you sound..." % user_input
    time.sleep(wait_time)
    print "Lets see who you are up agenst."
    time.sleep(wait_time)
    print ".."
    time.sleep(wait_time)

    return str(user_input)

# Picks an enemy name randomly from a list.
def choose_enemy():

    bad_guy_names = ["Mohammed Ali",
                     "Floyd Mayweather Jr.",
                     "Sugar Ray Robinson",
                     "Mike Tyson",
                     "Joe Louis",
                     "Manny Pacquiao",
                     "Joe Frazier",
                     "Rocky Marciano",
                     "Vasyl Lomachenko"]

    chosen_name = bad_guy_names[random.randint(0, len(bad_guy_names)-1)]
    print "Well if it aint none other than %s" % chosen_name
    time.sleep(wait_time)
    # dificulty options

    return str(chosen_name)

player_name = choose_name()
player_current_stamina = 0
player_max_stamina = 10
player_max_life = 10

enemy_name = choose_enemy()
enemy_current_stamina = 0
enemy_max_stamina = 10
enemy_max_life = 10

player = Boxer(name=player_name, life=player_max_life, stamina=player_current_stamina)
enemy = Boxer(name=enemy_name, life=enemy_max_life, stamina=enemy_current_stamina)

def game_loop():
    # The rounds of the game are controled by the value "turn", if it is 1 then
    # it is the players turn, if it is 0 then it is the computers turn.
    turn = 1
    # the game loop will continue as long as both players have life left.
    while player.life > 0 and enemy.life > 0:

        if turn == 1:

            player.stamina = player_max_stamina
            time.sleep(wait_time)
            print "Ok let's see what %s has got for %s" % (player.name, enemy.name)
            time.sleep(wait_time)
            while player.stamina > 0 and enemy.life > 0:
                print "Type jab, cross or haymaker."
                user_input = raw_input("> ")

                # TODO Make this one if/else, check it user

                if "jab" in user_input:
                    Moves().punch(user_input, player, enemy)
                elif "cross" in user_input:
                    Moves().punch(user_input, player, enemy)
                elif "haymaker" in user_input:
                    Moves().punch(user_input, player, enemy)
                else:
                    print "Try again..."
                    time.sleep(wait_time)
                    game_loop()

            turn = 0

        elif turn == 0:

            enemy.stamina = enemy_max_stamina
            time.sleep(wait_time)
            print "Now it's %s's turn to show %s his stuff." % (enemy.name, player.name)
            time.sleep(wait_time)
            while enemy.stamina > 0 and player.life > 0:
                # The computers moves are chosen at random

                # TODO Make this one if/else, check it user

                move_list = ['jab', 'cross', 'haymaker']

                enemy_move_choice = move_list[random.randint(0, len(move_list)-1)]

                if isinstance(enemy_move_choice,str):
                    Moves().punch(enemy_move_choice, enemy, player)
                else:
                    print "I broke now..."

                turn = 1

    if player.life <= 0:
        print "You suck %s! Your a looser!" % player_name
    elif enemy.life <= 0:
        print "%s just kicked %s's ass! !" % (player_name, enemy_name)
    else:
        print "I dont know how to get here."

game_loop()
