print('welcome to treasure quest')
choice1 = input('you are on the road where do you wanna go left or right\n').lower()
if choice1 == "left":
    print("congrats you survived the previos level")
    choice2 = input('you are on the sea shore do you want to wait or do you want to swim\n').lower()
    if choice2=="swim":
        print("You have just escaped death cause a tiger was chasing you....")
        choice=input('you have reached an island you have 3 doors "red", "blue","yellow" choose a door wisely to win the game\n ').lower()
        if choice=="red":
            print("hurray you have won the game  $$$$")
        else:
            print("game over")
    else:
        print("you have been eaten by a tiger....better luck next time")  
else:
    print("game over...")
