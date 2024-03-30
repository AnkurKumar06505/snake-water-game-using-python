import random
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp =="w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
        
print("The comp turn : snake(s), water(w), gun(g)")
randNO = random.randint(1,3)
if randNO == 1:
    comp = "s"
elif randNO == 2:
    comp = "w"
elif randNO == 3:
    comp = "g"


you = input("your turn: snake(s), water(w), gun(g)")

a = gamewin(comp,you)

print("the comp choose", comp)
print("you chose", you)

if a == None:
    print("The game is a tie !")
elif a:
    print("You win !")
else:
    print("You loose")
 