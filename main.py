import random

R = "rock"
P = "paper"
S = "scissors"

action_list = ["R", "P", "S"]

while True:
    Player_action = input("Enter a choice (R, P, S): ")                 
    CPU_action = random.choice(action_list)
    print(f"\nPlayer chose {Player_action}: CPU chose {CPU_action}.\n")

    if Player_action == CPU_action:
        print(f"Both players selected {Player_action}. It's a tie!")
        continue
    elif Player_action == "R":
        if CPU_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        break
    elif Player_action == "P":
        if CPU_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        break
    elif Player_action == "S":
        if CPU_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes sciccors! You lose.")
        break
    
    else:
        print("Error! Invalid action,select your input again") 
          


