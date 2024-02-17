import random

l = ["rock", "scissor", "paper"]

'''
rock vs paper--paper wins
rock vs scissor--scissor wins
paper vs scissor-- scissor wins
'''

ccount = 0
ucount = 0

while True:
    uc = int(input('''
        Game Start.....
        1.Yes
        2.No/Exit
        '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1.Rock
        2.Scissor
        3.Paper
                    '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            cchoice = random.choice(l)
            print("User choice: ", uchoice)
            print("Computer choice: ", cchoice)
            if uchoice == cchoice:
                print("It's a tie!")
            elif (uchoice == "rock" and cchoice == "scissor") or \
                (uchoice == "scissor" and cchoice == "paper") or \
                (uchoice == "paper" and cchoice == "rock"):
                print("User wins!")
                ucount += 1
            else:
                print("Computer wins!")
                ccount += 1
        print("User score: ", ucount)
        print("Computer score: ", ccount)
    elif uc == 2:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")