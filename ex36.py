
#the game is really difficult code I have print, the first time.

from sys import exit

def start():
    print """Welcome to the dark room.\nAnd there are three doors:[1], [2] and [3].\nWhich do you want to choose?"""
    begin()

def dead(reason):
    print reason, "I`m sorry, you have to die."
    exit(0)

def false_room():
    print "Since you don`t choose to back, I think you choose to insist. \nNext is a interesting room! One left door says 'Open me' while another in the right says 'Do not believe that door'. \nI need your decision!\n\tright or left?"
    hit7 = raw_input(">:")
    if hit7 == 'right':
        dead("A big stone falls off and strikes you. Told you not to believe! Alright~")
    elif hit7 == 'left':
        print "You get the gold in the next room! you`re the winner!"
        exit(0)
    else:
        dead("\nYou only have the two choices above!\n")
        
def door_colorful():
    print "Three doors again! But this time they are in different colors, \n\t[red], [bule] and [black]. \nWhich one to choose this time?"
    hit3 = raw_input(">:")
    if hit3 == 'bule':
        print "Unbelieveble! There`s a fish, alive! It will definetly be delicious~"
        hit4 = raw_input(">:")
        if 'eat' in hit4:
            dead("Your mother should tell you not to eat something you haven`t eaten before?")
        else:
            dead("The little fish suddenly become a big shark and chew you off.")
    elif hit3 == 'black':
        print "There are lots gold in the case. Would you take it?"
        hit5 =raw_input(">:")
        if 'back' in hit5 or 'no' in hit5:
            print "OK, maybe you`re right to choose not touch the gold and go back."
            door_colorful()
        else:
            dead("Don`t ask why.")
    elif hit3 == 'red':
        print "The room after red door has a man lifting a flower. He says 'Hey, tell you a secret, there are much gold behind the black door. Believe or not.', and he smiles then. \nDo you want turn back or just go through the room to the next?"
        hit6 = raw_input(">:")
        if 'back' in hit6:
            door_colorful()            
        else:
            false_room()
    else:
          dead("Godbye!")
            
def door_3():
    print "Hey, in the right hand, there`s a stone said 'Warrior, the treasure is in the deepths waiting for you!\nDo you want to explore next? Just go through the door in front of you."
    hit2 = raw_input(">:")
    if 'go' in hit2 or 'through' in hit2:
        door_colorful()
    else:
        dead("Oh coward, you don`t deserve to live.")

def begin():
    key = False    
    while True:
        print "Harry up, tell me your choice of the door."
        choose = raw_input(">:")
        if "1" == choose and key == False:
            print "Ok, in front of you is a table, and you`ll find a key on it, right?"
            print "So, you choose to 'get it and turn back' or 'stay for a while' then?"
            key = True
            hit1=raw_input(">:")
            if 'back' in hit1:
                print "Oh, here again. Then what`s your next choice?"
            elif 'stay' in hit1:
                dead("Why? I can`t understand your behavior!")
            else:
                dead("What do you want?")  
        elif "1" == choose and key == True:
            dead("Why you want to get there again???")         
        elif choose == "2":
            dead("Unfortunately, you fell into a dark hole.")
        elif "3" == choose:
            if key == False:
                print "I`m sorry, it seems the door is locked. Maybe the key is in other doors, choose one another?\n"
            if key == True:
                print "That`s the rignt key, conguatulation~!"
                door_3()
        else:
            print "Excuse me??? Please use English."
                
start()       
            
            
    
