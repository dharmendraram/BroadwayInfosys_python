# Computer vs human guessing rock,scissor,paper game using ramdom module
'''
Wins cases:
1. rock vs paper -> paper 
2. rock vs scissor -> rock
3. paper vs scissor -> scissor
'''
import random
game_list=["rock","scissor","paper"]

while True:
    cCount=0
    uCount=0
    uc=int(input('''
Rock Paper Scissor Game Start...
1. Yes
2. No / Exit
                 '''))
    
    if uc==1:
        for item in range(1,6):
            userInput=int(input('''
                        1. Rock
                        2. Scissor
                        3. Paper
                                
                                '''))
            if userInput==1:
                uChoice="rock"
            elif userInput==2:
                uChoice="scissor"
            elif userInput==3:
                uChoice="paper"
            else:
                print("Please enter the number (1,2,3) only")
                break

            cChoice=random.choice(game_list)
            if cChoice==uChoice:
                print(f"Computer value:{cChoice}")
                print(f"Human value:{uChoice}")
                print("Game Darw.......")
                cCount+=1
                uCount+=1
            elif (uChoice=="rock" and cChoice=="scissor") or (uChoice=="paper" and cChoice=="rock") or (uChoice=="scissor" and cChoice=="paper"):
                print(f"Computer value:{cChoice}")
                print(f"Human value:{uChoice}")
                print(f"Human win.......")
                uCount+=1
            else:
                print(f"Computer value:{cChoice}")
                print(f"Human value:{uChoice}")
                print(f"Computer win.......")
                cCount+=1
        print()
        if uCount==cCount:
            print(f"Human Score:{uCount}")
            print(f"Computer Score:{cCount}")
            print("Finally Game Draw.......")
        elif uCount>cCount:
            print(f"Human Score:{uCount}")
            print(f"Computer Score:{cCount}")
            print("Finally Human Win The Game .......")
        else:
            print(f"Human Score:{uCount}")
            print(f"Computer Score:{cCount}")
            print("Finally Computer Win The Game .......")
                        
    else:
        break