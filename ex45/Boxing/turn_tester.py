import time
turn = 1

while True:

    if turn == 1:
        while turn == 1:
            print "It is the players turn."
            time.sleep(1)
            print "It is the players turn."
            time.sleep(1)
            print "It is the players turn."
            time.sleep(1)

            turn = 0
    elif turn == 0:
        while turn == 0:
            print "It is the enemy turn."
            time.sleep(1)
            print "It is the enemy turn."
            time.sleep(1)
            print "It is the enemy turn."
            time.sleep(1)

            turn = 1
