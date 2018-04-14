import random
import time

wait_time = 1.5

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
        user.stamina = user.stamina - 10
        target.life = target.life - 10

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
player_max_stamina = 5
player_max_life = 50

enemy_name = choose_enemy()
enemy_max_stamina = 30
enemy_max_life = 50

player = Player(name = player_name, life = player_max_life, stamina = player_max_stamina)
enemy = Enemy(name = enemy_name, life = enemy_max_life, stamina = enemy_max_stamina)

# print vars(player)
# print vars(enemy)
#
# print player.print_stats()
# print enemy.print_stats()

def game_loop():
    print "Type jab, cross or haymaker."

    while player.life > 0 or enemy.life > 0:

        if player.stamina > 0 and enemy.life > 0:

            player.stamina = player_max_stamina

            while player.stamina > 0:
                user_input = raw_input("> ")

                if "jab" in user_input:
                    Moves().jab(player, enemy)
                    print "Take that!"
                    print "stamina: "+str(player.stamina)
                    print "life: "+str(enemy.life)
                elif "cross" in user_input:
                    Moves().cross(player, enemy)
                    print "And one of those!"
                    print "stamina: "+str(player.stamina)
                    print "life: "+str(enemy.life)
                elif "haymaker" in user_input:
                    Moves().haymaker(player, enemy)
                    print "And one of those!"
                    print "stamina: "+str(player.stamina)
                    print "life: "+str(enemy.life)
                elif "exit" in user_input:
                    exit(1)
                else:
                    print "Try again..."
                    time.sleep(wait_time)
                    game_loop()
        elif enemy.stamina > 0:

            enemy.stamina = enemy_max_stamina

            while enemy.stamina > 0 and player.life > 0:


                enemy_move_choice = random.randint(1,3)

                if enemy_move_choice == 1:
                    Moves().jab(enemy,player)
                    print "Oh, %s hits back with a jab!" % enemy_name
                    time.sleep(wait_time)
                    print "stamina: "+str(enemy.stamina)
                    print "life: "+str(player.life)
                    time.sleep(wait_time)
                elif enemy_move_choice == 2:
                    Moves().cross(enemy,player)
                    print "A cross from %s!" % enemy_name
                    time.sleep(wait_time)
                    print "stamina: "+str(enemy.stamina)
                    print "life: "+str(player.life)
                    time.sleep(wait_time)
                elif enemy_move_choice == 3:
                    Moves().haymaker(enemy,player)
                    print "%s throws the haymaker for the knockout!" % enemy_name
                    time.sleep(wait_time)
                    print "stamina: "+str(enemy.stamina)
                    print "life: "+str(player.life)
                    time.sleep(wait_time)
        else:
            if player.life < 0:
                print "You suck %s! Your a looser!" % player_name
                time.sleep(wait_time)
            elif enemy.life < 0:
                print "%s just kicked %s's ass! !" % (player_name, enemy_name)
            else:
                game_loop()


game_loop()
