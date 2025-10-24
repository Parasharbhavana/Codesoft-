import random

def get_choices():
    options = ["Rock", "Paper", "Scissor"]
    player_choice=input("Enter a choice (Rock , Paper , Scissor) :")


    if player_choice not in options:
        print("Invalid choice ! Please try again.")
        return get_choices()

    computer_choice= random.choice(options)
    choices={"player" : player_choice , "computer" : computer_choice}
    return choices

def check_win(player , computer):
    print(f"You chose {player.capitalize()}, computer chose {computer.capitalize()}.")
    if player == computer:
        return "It's a tie !"
    elif player == "Rock":
        if computer == "Scissor" :
            return "Rock smashes scissor ! You win."
        else:
            return "Paper covers rock ! You lose."

    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers rock ! You win."
        else:
            return "Scissor cuts paper ! You lose."

    elif player == "Scissor":
        if computer == "Paper":
            return "Scissor cuts paper! You win."
        else:
            return "Rock smashes scissor ! You lose. "
while True:
  choices = get_choices()
  result = check_win(choices["player"],choices["computer"])
  print(result)


  play_again = input("Do You want to play again ? (yes/no) :")
  if play_again != "yes":
      print("Thanks for playing !")
      break
