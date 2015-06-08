import random
def name_to_number(name):
    if name == "rock":
        return 0
    elif name =="Spock":
        return 1
    elif name =="paper":
        return 2
    elif name =="lizard":
        return 3
    elif name =="scissors":
        return 4
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else :
        return "scissors"
    

comp_number = random.randrange(0,4)
comp_choice = number_to_name (comp_number)
    
def rpsls(player_choice):
    player_number =  name_to_number(player_choice)
    result =(player_number - comp_number ) % 5
    if result == 1 or result == 2:
        print "Player chooses " + player_choice
        print "Computer chooses " + comp_choice   
        print "Player wins!"
        print " "
    elif result == 3 or result == 4 :
        print "Player chooses " + player_choice
        print "Computer chooses " + comp_choice        
        print "Computer wins!"
        print " "
    else :
        print "Player chooses " + player_choice
        print "Computer chooses " + comp_choice   
        print "player and computer take a draw."
        print " "
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
               
    





