from sys import exit
from random import randint
import time

class Room(object):

    def enter(self):
        print "There should be a Room() here, It has not been made yet."

        exit(1)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.inventory = []

class Engine(object):

    def __init__(self,room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()

        while True:
            print "\t\n,',',',','\n"
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)


class Intro(Room):
    def enter(self):
        print """
----
A call to adventure calls you.

Do you take up the call?
----
        """

class Hub(Room):
    pass

class Item1(Room):
    pass

class Item2(Room):
    pass

class Boss(Room):
    pass

class Win(Room):
    pass

class Lose(Room):
    pass

class Map(object):

    rooms = {
    'intro': Intro(),
    'hub': Hub(),
    'item_1': Item1(),
    'item_2': Item2(),
    'boss': Boss(),
    'win': Win(),
    'lose': Lose()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        return Map.rooms.get(room_name)

    def opening_room(self):
        return self.next_room(self.start_room)

player = Player('Carl')
a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()
