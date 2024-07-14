import random
result="draw"
while result == "draw":
    print("")
    choise=input("Choose \n 1 for rock \n 2 for paper \n 3 for scissor\n ")
    player=int(choise)
    while  player < 1 or player > 3 :
        print("wrong")
        choise=input("Choose \n 1 for rock \n 2 for paper \n 3 for scissor\n ")
        player=int(choise)
    print("nice choise")
    cpu=random.randrange(1,3)
    print("your opponent chose",cpu)
    if (cpu == 1 and player == 2) or (cpu == 2 and player == 3) or (cpu == 3 and player == 1):
        result=("win")
        print("YOU WON")
    if (cpu == 1 and player == 3) or (cpu == 2 and player == 1) or (cpu == 3 and player == 2):
        result=("lose")
        print("YOU LOSE")
    if player==cpu:
        print("DRAW")
        result=("draw")