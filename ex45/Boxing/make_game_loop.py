import random
import time

wait_time = .5

class Moves(object):
    # def __init__(self, user, target):
    #     self.user = user
    #     self.target = target

    def jab(self, user, target):
        user.stamina = user.stamina - 2
        target.life = target.life - 3

    def cross(self, user, target):
        user.stamina = user.stamina - 5
        target.life = target.life - 6

    def haymaker(self, user, target):
        user.stamina = user.stamina - 1
        target.life = target.life - 999

class Boxer(object):
    def __init__(self, name = '', life = 0, stamina = 0):
        self.name = name
        self.life = life
        self.stamina = stamina

    def print_stats(self):
        print "name: "+self.name
        print "life: "+str(self.life)
        print "stamina: "+str(self.stamina)

class Player(Boxer):
    pass


class Enemy(Boxer):
    pass

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
enemy_name = choose_enemy()


player = Player(name = player_name, life = 10, stamina = 10)
enemy = Enemy(name = enemy_name, life = 10, stamina = 10)

# print vars(player)
# print vars(enemy)
#
# print player.print_stats()
# print enemy.print_stats()

def game_loop():
    print "Type play or pass"

    while player.life > 0 and enemy.life > 0:
        user_input = raw_input("> ")

        if "play" in user_input:
            player.print_stats()
        elif "jab" in user_input:
            Moves().jab(player, enemy)
            print "Take that!"
        elif "cross" in user_input:
            Moves().cross(player, enemy)
            print "And one of those!"
        elif "haymaker" in user_input:
            Moves().haymaker(player, enemy)
            print "And one of those!"
        elif "exit" in user_input:
            exit(1)
        else:
            print "Try again..."
            time.sleep(wait_time)
            game_loop()

    print "%s just kicked %s's ass! !" % (player_name, enemy_name)

game_loop()
