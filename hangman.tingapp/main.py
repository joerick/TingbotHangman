import tingbot
from tingbot import *
import random
import time
file = open('word_list.txt')

# setup code here
otherbtn = False
HANGMAN = (
"""
 ------ 
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",    
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

WORDS = []
for line in file:
    line = line.strip()
    line = line.upper()
    WORDS.append(line)

#WORDS = ('ROBERT', 'TEST', 'PYTHON', 'TINGBOT')
def wait(duration):
    from tingbot.run_loop import main_run_loop
    import time
    main_run_loop._wait(time.time() + duration)

def text(word):
    screen.fill(color = 'black')
    y=15
    
    for line in str(word).splitlines():
        screen.text(line, xy=(10, y), align = 'left')
        y += 22
    screen.update()
MAX_WRONG = len(HANGMAN) - 1

word = random.choice(WORDS)   
so_far = '-' * len(word) 
wrong = 0                     
used = []                     
alphabet_i = 1
keyboard = False
def clear():
    screen.fill(color='black')
    screen.update()
@button.press('right')
def right():    
    global lastbtnpress

    lastbtnpress = 'right'
    otherbtn = True
@button.press('left')
def left():
    global lastbtnpress

    lastbtnpress = 'left'
    otherbtn = True
@button.press('midright')
def select():
    global lastbtnpress

    lastbtnpress = 'select'
    otherbtn = True
@button.press('midleft')
def select():
    global lastbtnpress

    lastbtnpress = 'select'
    otherbtn = True
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
count = 1
lastbtnpress = None
def loop():
    
    global wrong
    global so_far
    global word
    if wrong < MAX_WRONG and so_far != word:
        wait(1)
        text(str(HANGMAN[wrong]))
        wait(2.5)
        clear()
        text("You've used the\n following letters:")
        wait(2)
        screen.update()
        for k in used:
            text(str(k))
            wait(0.5)
        clear()
        text("So far, \nthe word is:\n" +  str(so_far))
        wait(2)
        clear()
        global alphabet_i
        global lastbtnpress
        while True:
            if lastbtnpress == 'left':
                alphabet_i -= 1
            elif lastbtnpress == 'right':
                alphabet_i += 1
            elif lastbtnpress == 'select':
                used.append(alphabet[alphabet_i - 1])
                break
            text(alphabet[alphabet_i - 1])
            lastbtnpress = None
            wait(0.1)
        if str(alphabet[alphabet_i - 1]) in str(word):
            text('Yes! ' + alphabet[alphabet_i - 1] + ' is in \n the word!')
            wait(1)
            new = ""
            for i in range(len(word)):
                if alphabet[alphabet_i - 1] == word[i]:
                    new += alphabet[alphabet_i - 1]
                else:
                    new += so_far[i]              
            so_far = new
        else:   
            text('Sorry, ' + alphabet[alphabet_i - 1] + ' is not \n in the word.')
            wait(1)
            wrong += 1
        alphabet_i = 1
        lastbtnpress = None
    else:
        if wrong == MAX_WRONG:
            text(HANGMAN[wrong])
            wait(1)
            text('YOU HAVE BEEN \n HANGED, GET R3KD M8')
            clear()
            text('The word was:')
            wait(1)
            clear()
            text(word)
            wait(1)
            clear()
        else:
            text('WOO HOO \n , YOU DID IT!')
            wait(1.5)
            clear()
            text('The word was:')
            wait(1)
            clear()
            text(word)
            wait(1)
            clear()
        wait(4)
        clear()
    # run the app
tingbot.run(loop)
            