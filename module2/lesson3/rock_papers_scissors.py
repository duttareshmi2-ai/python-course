import random

from rich import print as p

VALID_CHOICES = ["rock", "paper", "scissors"]


def user_choice():
    choice = input("Enter rock, paper, or scissors: ").strip().lower()

    if choice in VALID_CHOICES:
        p(f"[yellow]You chose[/yellow] [blue]{choice}[/blue]")
        return choice

    p("[red]Invalid Input![/red]")
    return user_choice()


def ai_choice():
    choice = random.choice(VALID_CHOICES)
    p(f"[yellow]AI chose[/yellow] [blue]{choice}[/blue]")
    return choice


def check_win(player_choice, ai_choice_value):
    player_choice = player_choice.lower()
    ai_choice_value = ai_choice_value.lower()

    if player_choice == ai_choice_value:
        p("[grey]Draw![/grey]")
    elif (player_choice == "paper" and ai_choice_value == "rock") or \
         (player_choice == "scissors" and ai_choice_value == "paper") or \
         (player_choice == "rock" and ai_choice_value == "scissors"):
        p("[green]You win![/green]")
    else:
        p("[red]AI wins![/red]")


def main():
    while True:
        player = user_choice()
        computer = ai_choice()
        check_win(player, computer)

        replay = input("Do you want to play again? (yes/no): ").strip().lower()

        if replay != "yes":
            p("[cyan]Thanks for playing![/cyan]")
            break


if __name__ == "__main__":
    main()
