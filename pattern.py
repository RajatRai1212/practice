
import random
print("PRESS Y TO PLAY THE GAME")
q= input()
pc= random.randint(1,33)
if q=="y":

    print("CHOOSE A NUMBER BETWEEN 1-33")
    n = input()

    if n == pc:
        print("Congrats!!!!!!!!")

    else:
        print("U lost the computer picked ",pc)
else:
    print("dont play then... ;-( ")

