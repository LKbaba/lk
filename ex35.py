#I guess there something with 'dead', I`m wrong again,,,,, just exit the code, and the author define the 'dead' in the bottom.
from sys import exit

def gold_room():
    #don`t know where is wrong... :(, get it!
    print "It`s really a lot of money, How much do you want?"
    while True:
        money = raw_input("> ")
        if money.isdigit():
            #to change the number to a max integer below the number.
            oh = int(money)
            if oh < 20:
                print "You`re not greedy, nice."         
                exit(0)
            else:
                print "Oh, you`re little bad bad. try again?"
        else:
            print "Pradon, I don`t think you input a number."
    
    #print "This room is full of gold. How much do you take?"
    #next = raw_input("> ")
    
    #'judge the input is or not a number', that`s completly wrong~, just to judge whether there is '0' or '1' in your input.
    #if "0" in next or "1" in next:
    
    #is a command is to judge if there is only 'number' in next.
    #if next.isdigit():
        
        #'int' means what?
        #how_much = int(next)
    
    #else:
        #dead("Man, learn to type a number.")
    
    #if how_much < 50:
        #print "Nice, you`re not greedt, you win!"
        
        #? just to exit the code.
        #exit(0)
    
    #else:
        #dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    #this way of judgement is really amazing!
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
            
        elif next == "taunt bear" and not bear_moved:
            print "The bears has moved from the door. You can go through it now."
            #change the True, genius!
            bear_moved = True
        #this step can aviod the wrong circle.
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chew your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, what ever stares at you and you go insane."
   
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
   
    #a new way to judge
    if "flee" in next:
        start()
    #'in next' means if it appear then you can do the command followed. So do all 'in next'.
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


#I have a lot of questions! Oh my God
def dead(why):
    #',' will be a space in the display and '+' not.
    print why,"Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        

start()
