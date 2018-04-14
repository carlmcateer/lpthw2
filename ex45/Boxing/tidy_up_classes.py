import random
import time

wait_time = 1.5

class Moves(object):

    def jab(self, user, target):
        miss_chance = 1
        if miss_chance < random.randint(1,10):
            user.stamina = user.stamina - 2
            target.life = target.life - 2
            time.sleep(wait_time)
            print "%s lands a beutiful jab!" % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)
        else:
            user.stamina = user.stamina - 2
            target.life = target.life - 0
            time.sleep(wait_time)
            print "%s can't find his range with the jab!" % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)


    def cross(self, user, target):
        miss_chance = 5
        if miss_chance < random.randint(1,10):
            user.stamina = user.stamina - 5
            target.life = target.life - 5
            time.sleep(wait_time)
            print "A cross landed stright down the pipe by %s" % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)
        else:
            user.stamina = user.stamina - 5
            target.life = target.life - 0
            time.sleep(wait_time)
            print "Ohh %s does not connect with the cross!" % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)

    def haymaker(self, user, target):
        miss_chance = 9
        if miss_chance < random.randint(1,10):
            user.stamina = user.stamina - 10
            target.life = target.life - 10
            time.sleep(wait_time)
            print "I cant believe it! A wild haymaker lands for %s!!!" % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)
        else:
            user.stamina = user.stamina - 10
            target.life = target.life - 0
            print "Swing and a miss for %s, that haymaker wasent even close." % user.name
            print "%s stamina: " % user.name + str(user.stamina)
            print "%s life: " % target.name + str(target.life)
            time.sleep(wait_time)

class Boxer(object):
    def __init__(self, name = '', life = 0, stamina = 0):
        self.name = name
        self.life = life
        self.stamina = stamina


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

def choose_enemy():

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

    chosen_name = bad_guy_names[random.randint(0, len(bad_guy_names)-1)]
    print "Well if it aint none other than %s" % chosen_name
    time.sleep(wait_time)
    #dificulty options

    return str(chosen_name)

player_name = choose_name()
player_current_stamina = 0
player_max_stamina = 10
player_max_life = 10

enemy_name = choose_enemy()
enemy_current_stamina = 0
enemy_max_stamina = 10
enemy_max_life = 10

player = Boxer(name = player_name, life = player_max_life, stamina = player_current_stamina)
enemy = Boxer(name = enemy_name, life = enemy_max_life, stamina = enemy_current_stamina)

def game_loop():
    turn = 1
    while player.life > 0 and enemy.life > 0:



        if turn == 1:

            player.stamina = player_max_stamina
            time.sleep(wait_time)
            print "Ok let's see what %s has got for %s" % (player.name, enemy.name)
            time.sleep(wait_time)
            while player.stamina > 0 and enemy.life > 0:
                print "Type jab, cross or haymaker."
                user_input = raw_input("> ")

                if "jab" in user_input:
                    Moves().jab(player, enemy)
                elif "cross" in user_input:
                    Moves().cross(player, enemy)
                elif "haymaker" in user_input:
                    Moves().haymaker(player, enemy)
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

                enemy_move_choice = random.randint(1,3)

                if enemy_move_choice == 1:
                    Moves().jab(enemy,player)
                elif enemy_move_choice == 2:
                    Moves().cross(enemy,player)
                elif enemy_move_choice == 3:
                    Moves().haymaker(enemy,player)

                turn = 1

    if player.life <= 0:
        print "You suck %s! Your a looser!" % player_name
    elif enemy.life <= 0:
        print "%s just kicked %s's ass! !" % (player_name, enemy_name)
    else:
        print "I dont know how to get here."


game_loop()
