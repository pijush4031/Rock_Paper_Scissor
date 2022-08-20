# rock vs paper -> paper wins
# rock vs scissor -> rock wins
# paper vs scissor -> scissor wins

import random
l=["Rock","Paper","Scissor"]
while True:
    Ucount=0
    Ccount=0
    print("Want to play??")
    user_choice=int(input('''
    1 Yes
    2 No | Exit
    '''))
    if user_choice==1:
        print("Game starts........")

        for i in range(1,6):
            UserInput=int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            # User choice
            if UserInput==1:
                UserChoice="Rock"
            elif UserInput==2:
                UserChoice="Paper"
            elif UserInput==3:
                UserChoice="Scissor"
            else:
                print("Invaild choice!!!!")
            com=random.choice(l)  # Computer random choice from the list
            print("Your choice is: ",UserChoice)
            print("Computer choice is: ",com)
            print(" ")

            # Logic------->
            if (UserChoice=="Rock" and com=="Scissor") or (UserChoice=="Paper" and com=="Rock") or (UserChoice=="Scissor" and com=="Paper"):
                print("You win....")
                Ucount+=1
                print("Your point is: ",Ucount)
                print("Computer point is: ",Ccount)
            elif UserChoice==com:
                print("Oops same choice.....")
                Ucount+=1
                Ccount+=1
                print("Your point is: ",Ucount)
                print("Computer point is: ",Ccount)
            else:
                print("Computer Win")
                Ccount+=1
                print("Your point is: ",Ucount)
                print("Computer point is: ",Ccount)

        print(" ")
        # logic to decide who is winner
        if Ucount>Ccount:
            print("Congo!!!!You win the game")
        elif Ucount==Ccount:
            print("Game is draw.")
        else:
            print("Oops!!!!Computer wins the game")
        print(" ")
    else:
        break