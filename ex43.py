from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"

        exit(1)


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------"
            next_scene_name = current_scene_name.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You Died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a luser",
        "I have a small puppy that is better at this."
    ]

    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        # Opening Dialog
        input = raw_input("> ")

        if input =="option1":
            #dialog 1 leading to death
            return 'death'

        elif input == "option2":
            #dialog 2 leading to death
            return 'death'

        elif input == "option3":
            #dialog 3 leading to the right answer
            return 'laser_wepon_armory'

        else:
            #dialog 4 leading to returning to the coridor, this is if they
            #get none of the right input's
            return 'central_coridor'

class LaserWeponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
