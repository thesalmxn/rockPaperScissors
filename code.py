import random

def win(c,h):
    if(c=="rock"):
        if(h == "paper"):
            return "You Win"
        elif(h == "rock"):
            return "It's a Tie"            
        elif(h == "scissors"):
            return "Computer Wins"
        
    elif(c == "paper"):
        if(h == "scissors"):
            return "You win"
        elif(h == "paper"):
            return "It's a Tie"
        elif(h == "rock"):
            return "Computer Wins"
        
    elif(c == "scissors"):
        if(h == "rock"):
            return "You Win"
        elif(h == "scissors"):
            return "It's a Tie"
        elif(h == "paper"):
            return "Computer Wins"
        
    
    
# Driver    
li_rps = ["rock","paper","scissors"]
computer_hand = random.choice(li_rps)
# print("Rock : R \nPaper : P \nScissors : S")
print("rock \npaper \nscissors \n")
human_hand = input("Enter your choice : ")
print("Computer chose '{}' and you chose '{}'".format(computer_hand,human_hand))
print(win(computer_hand,human_hand))
