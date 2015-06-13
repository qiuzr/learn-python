# 猜数字游戏
import simplegui
import random
my_guess = 0
step = 0
number = 0


def range100():
    global step
    global number
    step = 7
    print "New game , range is from 0 to 100 "
    print "Number of remaining guesses is " , step 
    
#在0到100之间取一个随机数   
    number = random.randrange(0,100)


def range1000():
    global step
    global number
    step = 10
    print "New game , range is from 0 to 1000 "
    print "Number of remaining guesses is " , step
    
#在0到1000之间取一个随机数   
    number = random.randrange(0,1000)
    
    

def new_game():
    range100()
    
    
def input_guess(guess):
    
    global my_guess
    global number
    global step
    
    my_guess = int (guess) 
    
    print "Guess was ", my_guess
    if my_guess < number:
        print "Higher!"
        step = step - 1
        print "Number of remaining guesses is " , step
        print " "

    elif my_guess > number:
        print "Lower!"
        step = step - 1
        print "Number of remaining guesses is " , step
        print " "
    else :
        print "Correct! "
        print " "
        new_game()

    
# create frame

frame = simplegui.create_frame("guess_number",200,200)

button1 = frame.add_button('range from 0 to 100', range100 ,200)
button2 = frame.add_button('range from 0 to 1000', range1000 ,200)
guess = frame.add_input('enter a guess', input_guess , 200)

#new_game()
new_game()

# always remember to check your completed program against the grading rubric
