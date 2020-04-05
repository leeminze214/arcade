"""1 pm, 11/24/2019
guess the number project#1"""


from random import randint
from time import sleep

THESCORE = 0
def gues():
    global THESCORE
    while True:
        print ("Guess the a number btwn 1 - 20, if you guess it right you get 5 points towards your account")

        wrong = ["goodshit, that mean u aint so gay aft all","good one... rise of homophobes!!!", "yeye miss us wit those gay shit"]
        chances = 3
        cn = randint(1,20)
        quit = False
        while chances > 0 and quit != "y":
            print ("okay so you have "+str(chances)+" chances")
            ug = int(input("guess a fkin number or ur balls are gone:____"))
            print(cn)
            if ug > 20 or ug < 0:
                print ("oh helllnahhh. gtfo u dumbass lmao")
                break
            elif cn == ug:
                    print ("mhmmm, unusually quick... ")
                    sleep(1)
                    print ("wel yes the number was "+str(cn)+". you got 5 points")
                    THESCORE += 5
                    break
            elif cn != ug:
                    sleep(1)
                    print (wrong[randint(0,2)]) #has to be len() minus one since len gives the abs, but we count form 0
                    chances -= 1
                    if chances > 0 and cn < ug:
                        print ("its a lil smaller")
                        print ("if you enter somthing bigger i swear")
                        print ("")
                        
                    elif chances > 0 and cn > ug:
                        print ("its bigger")
                        print ("")                
        quit = input("y for yes, any for no")
            
        
        if quit == "y":
            print(f"you earned {THESCORE} points")
            break
        
    return THESCORE

       
    
"""
testing 
b = "a"
c = 4+4
c = str(c)
print (c + b)

"""
