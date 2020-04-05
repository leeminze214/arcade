'''
Write a programme, which generates a random password for the user. Ask the user how long they want their password
to be, and how many letters and numbers they want in their
password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.
'''
import time
import random
import json

lows = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
caps = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
nums = "1,2,3,4,5,6,7,8,9,0"
symb = "!,@,#,$,%,*"
lows = lows.split(",")
caps = caps.split(",")
nums = nums.split(",")
symb = symb.split(",")


#chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%*'
with open('storage.json') as a:
    storage = json.load(a)
    
def woww(enter):
    global storage
    if enter == "S":
    #if user wants to sign in
        while True:
            username = input("Create Username:")
            
            if username.strip() not in storage:
                a = generator()
                print(f"Your Password Is: {a}")
                storage[username] = {}
                storage[username]["password"] = a
                entering = input("Would u like to log in? any for yes, n for no")
                break
            else:
                print(f"{username} It is already taken!")
            
    if enter == "L" or entering.lower() != "n":
    #if user decides to log in from the start or immediately after creating a new account
        
        attempts = 0
        while attempts < 3 :
        #limits the number of attempts
            print("\nLog in")
            oun = input("username:  ")
            opw = input("password:  ")
            temoun = oun.strip( )
            temopw = opw.strip()
            
            if temoun in list(storage.keys()) and temopw == storage[temoun]["password"]:
                #if the input is a pair within the json file
                
                temtime = time.strftime('%X %x')
                
                if "time" in storage[temoun]:
                #if it has been logged in before, show "last logged in"
                    print("welcome back master chief")
                    print(f"last log on was:  {temtime}")
                else:
                    print(f"Welcome {temoun}!!")
                storage[temoun]["time"] = temtime
                #updates the "last logged on" time
                #files(temoun,temopw)
                with open('storage.json','w') as a:
                    json.dump(storage, a)
                thegames(temoun,temopw)
                
                break
            
            else:
                #if it was an invalid login
                print("\nInvalid Login")
                attempts += 1

                if attempts != 3:
                    print(f"you have {3-attempts} more attempts")
                    
                elif attempts == 3:
                    print("sorry, too many attempts")
        
def generator(length = 2):#this multiplies it by 4 due to the for loop below
    npw = ''
    while True:
        for i in range(length):
            npw += random.choice(lows)
            npw += random.choice(caps)
            npw += random.choice(nums)
            npw += random.choice(symb)
        if npw not in storage:
            return npw
            break
        
def start():
    global storage
    print("yo welcome to PWEE")
    print(storage)

    
    while True:
        enter = input('signup --- S. log in --- L')
        if enter.upper() != "S" and enter.upper() != "L":
            print("Choose to signup or log in")
        #user picks to either make new account or log in to existing account
        else:
            woww(enter)
            with open('storage.json','w') as a:
                json.dump(storage, a)
            #updates the file at the end
            break
            

def thegames(temoun,temopw):
    global storage
    import subgame
    import hangman
    thechoice = input("play guess/hang:  ")
    if thechoice == "guess":
        thescore = subgame.gues()
    elif thechoice == "hang":
        thescore = hangman.HANG()
    if "score" not in storage[temoun]:
        storage[temoun]["score"] = thescore
    else:
        storage[temoun]["score"] += thescore

 
start()




