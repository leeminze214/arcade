
from random import randint
from time import sleep
import string
THESCORE = 0
def gues():
    global THESCORE
    while True:
        print ("Guess the a number btwn 1 - 20, if you guess it right \nyou get 5 points towards your account")

        wrong = ["good try... you didnt get it tho","mhm, not quite"]
        chances = 3
        cn = randint(1,20)
        quit = False
        while chances > 0 and quit != "y":
            print ("okay so you have "+str(chances)+" chances")
            while True:    
                ug = input("guess a number (1-20 inclusive):____")
                check = [str(i) for i in range(21)]
                
                if ug in string.ascii_letters:
                    print("no letters")
                    
                if ug in "`~!@#$%^&*()+_-=<>?,./{}[]\|":
                    print("no symbols")
                    
                if ug in check:
                    break                         
                
            if cn == int(ug):
                    print ("nice you got it right! ")
                    sleep(1)
                    print ("you got 5 points")
                    THESCORE += 5
                    break
            elif cn != ug:
                    sleep(1)
                    print (wrong[randint(0,1)]) #has to be len() minus one since len gives the abs, but we count form 0
                    chances -= 1
                    if chances > 0 and cn < int(ug):
                        print ("its a lil smaller\n")
                       
                        
                    elif chances > 0 and cn > int(ug):
                        print ("its bigger\n")
                                       
        quit = input("y for quit, any for stay")
            
        
        if quit == "y":
            print(f"you earned {THESCORE} points")
            break
        
    return THESCORE



