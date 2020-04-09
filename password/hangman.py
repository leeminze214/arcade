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

def givehint(word,length, hintcount):    
    clues = input("would you like a clue\n1 for no,any for yes")
    if clues != "1":
        hintcount += 1
        while True:
            a = random.choice(range(length))
            thehint = word[a]
            if thehint not in HANG.subs:
                break
        bb = []
        for i in range(length):
            if word[i] == thehint:
                bb.append(i)
                
                        
        for i in bb:
            HANG.subs[i] = thehint
     
    print("".join(HANG.subs))
    
        
def playing():
    play = input("\n1 for exit, any for play\n")
    return play

def asterisks():
    
    print("\nThe word is:  "+''.join(HANG.subs))

def guessing(attempts):
    global guess
    while True:
        symbol = False
        guess = input("Your guess is:\n  ")
        if guess in attempts:
            print("you already tried that")
        for i in guess:
            if i not in string.ascii_letters:
                symbol = True
        if symbol == True:
            print("no symbol or number")
        if guess in HANG.subs and guess != "*":
            print("you already got that!")
        if len(guess) > HANG.length:
            print("that is longer than the actual word is")
        if symbol == False and guess not in HANG.subs and guess not in attempts:
            attempts.append(guess)
            break
         
def judge(word,length):
    global guess
    
    if guess.lower() == word:
        HANG.subs = word
        print(f"woeeee...ya the word was {word}")
       
    elif guess.lower() in word and len(guess) == 1:
        indexsofletter = []
        for i in range(length):
            if word[i] == guess.lower():
                indexsofletter.append(i)

        for i in indexsofletter:
            HANG.subs[i] = guess.lower()
        time.sleep(0.5)
        print("nice you got it")
        
    elif guess.lower() in word:
        print("one letter at a time,,, or if you so good, guess the whole word")
        print("I wont tell you if thats right or wrong.....")
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
            print("Guess one letter at a time, \nOr guess the whole word if you are 'So gOoD")
            word = random.choice(words)
            HANG.length = len(word)
            HANG.subs = [ "*" for i in range(HANG.length)]
            guess =""
            HANG.hangindex = 0
            attempts = []
            hintcount = 0
            
            while HANG.hangindex < len(pics)-1:
                
                if word == "".join(HANG.subs)and hintcount > HANG.length -2:
                    print(f"you won... but with {hintcount} hints...only 15 points earned")
                    play = playing()
                    THESCORE += 15
                    break
                elif word == "".join(HANG.subs):
                    print("you won, and earned 25 points")
                    
                    THESCORE += 25
                    break
                hangman()
                asterisks()
                givehint(word,HANG.length,hintcount)
                if "".join(HANG.subs) != word:
                    guessing(attempts)
                    judge(word,HANG.length)
        else:
            print(f"okay, you earned {THESCORE} points")
            return THESCORE
            break









