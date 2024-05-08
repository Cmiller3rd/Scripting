import random
rounds = int(input("How many rounds would you like to play? "))
while rounds > 0:
    my_score = 0
    comp_score = 0
    computer = {1: "rock", 2: "scissors", 3: "paper"}
    computer_list = list(computer.keys())
    comp_key = random.choice(computer_list)
    comp_value = computer[comp_key]

    mine = input("rock, paper, scissors, shoot! ").lower()

    if mine == comp_value:
        print("We tied!")
    else:
        if comp_value == "rock" and mine == "scissors":
            print("You lose! I chose rock")
            comp_score += 1
        elif comp_value == "rock" and mine == "paper":
            print("You win! I chose rock")
            my_score += 1
        elif comp_value == "paper" and mine == "rock":
            print("You lose! I chose paper")
            comp_score += 1
        elif comp_value == "paper" and mine == "scissors":
            print("You win! I chose paper")
            my_score += 1
        elif comp_value == "scissors" and mine == "paper":
            print("You lose! I chose scissors")
            comp_score += 1
        elif comp_value == "scissors" and mine == "rock":
            print("You win! I chose scissors")
            my_score += 1
    rounds -= 1
print(f"Final Score: \nComputer: {comp_score}\nYou: {my_score}")