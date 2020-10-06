from random import randint 

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 

t = ["Rock","Paper","Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock,Paper,Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win!",player,"smashes",computer) 
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!",computer,"cut",player)
        else:
            print("You win!",player,"covers",computer) 
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!",computer,"smashes",player)
        else:
            print("You win!",player,"cut",computer) 
    else:
        print("That's not a valid play. Check your spelling!") 
    player = False
    computer = t[randint(0,2)]    