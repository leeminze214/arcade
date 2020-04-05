#april 4h 2020 2:23 am, yes am
import random
import string
import time

pics = [
'''


  +---+

   |   |

       |

       |

       |

       |

  =========''', '''



    +---+

    |   |

    O   |

        |

        |

        |

  =========''', '''



    +---+

    |   |

    O   |

    |   |

        |

        |

  =========''', '''



    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''', '''



    +---+

    |   |

    O   |

   /|\  |

        |

        |

  =========''', '''



    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''', '''



    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

  =========''']


with open('words.txt') as words:
    words = words.read()
    words = words.split('\n')

def givehint(subs,word,length, hintcount):    
    clues = input("would you like a clue\n1 for no,any for yes")
    if clues != "1":
        hintcount += 1
        while True:
            a = random.choice(range(length))
            thehint = word[a]
            if thehint not in subs:
                break
        bb = []
        for i in range(length):
            if word[i] == thehint:
                bb.append(i)
                
                        
        for i in bb:
            subs[i] = thehint
     
    print("".join(subs))
    
        
def playing():
    play = input("\n1 for exit, any for play\n")
    return play

def asterisks(subs):
    
    print("\nThe word is:  "+''.join(subs))

def guessing(attempts,subs):
    global guess
    while True:
        guess = input("Your guess is:\n  ")
        if guess in attempts:
            print("you already tried that")
   
        if guess not in string.ascii_letters:
            print("no symbol or letters")
        if guess in subs and guess != "*":
            print("you already got that!")
        if guess in string.ascii_letters and len(guess) == 1 and guess not in subs and guess not in attempts:
            attempts.append(guess)
            break
         
def judge(word,subs,length):
    global guess
    if guess in word:
        indexsofletter = []
        for i in range(length):
            if word[i] == guess:
                indexsofletter.append(i)

        for i in indexsofletter:
            subs[i] = guess
        time.sleep(0.5)
        print("nice you got it")
        
    else:
        time.sleep(0.5)
        print("nope u didnt get it")
        HANG.hangindex += 1
    time.sleep(1)
    
def hangman():
    
    print(pics[HANG.hangindex])
    time.sleep(0.5)
    
def HANG():
    THESCORE = 0
    while True:
        play = playing()
        if play != '1':

            word = random.choice(words)
            length = len(word)
            subs = [ "*" for i in range(length)]
            guess =""
            HANG.hangindex = 0
            attempts = []
            hintcount = 0
            
            while HANG.hangindex < len(pics)-1:
                
                if word == "".join(subs)and hintcount > length -2:
                    print(f"you won... but with {hintcount} hints...only 15 points earned")
                    play = playing()
                    THESCORE += 15
                    break
                elif word == "".join(subs):
                    print("you won, and earned 25 points")
                    
                    THESCORE += 25
                    break
                hangman()
                asterisks(subs)
                givehint(subs,word,length,hintcount)
                if "".join(subs) != word:
                    print(word)
                    guessing(attempts,subs)
                    judge(word,subs,length)
        else:
            print(f"okay, you earned {THESCORE} points")
            return THESCORE
            break














