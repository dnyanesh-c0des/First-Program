import rich 
import pyfiglet
import random

from rich.console import Console
console=Console()


guess_game_title = pyfiglet.figlet_format("GUESS HIGHER OR LOWER GAME", font="bubble")

print(guess_game_title)

console.print("[bold green]Welcome to the Guess Higher or Lower Game![/bold green]")
print("\n")
console.print("[bold cyan] Rules of the Game:[/bold cyan]")
console.print("[cyan]1. The computer will randomly select a number between 1 and 100.[/cyan]")
console.print("[cyan]2. The generated number will be displayed.[/cyan]")
console.print("[cyan]3. Then the computer will randomly select another number between 1 and 100.[/cyan]")
console.print("[cyan]4. You have to guess whether the second number is higher or lower than the first number.[/cyan]")
console.print("[cyan]5. If you guess correctly, you win! If you guess incorrectly, you lose.[/cyan]")
console.print("[cyan]6. You can play multiple rounds and keep track of your score.[/cyan]")
print("\n")
console.print("[bold magenta]Let's start the game![/bold magenta]")
console.print("[bold yellow]Good luck![/bold yellow]")


random_integer = random.randint(1, 100)
print(f"The number generated is: {random_integer}")
console.print("[bold cyan]Now, guess whether the next number will be higher or lower than the generated number.[/bold cyan]")


while True:
    user_guess = input(f" Please enter your guess (higher/lower) or 'h'/'l' and enter exit to quit: ")
    if user_guess.lower() == "exit":
        console.print("[bold orange]Thanks for playing! Goodbye![/bold orange]")
        break
    random_integer2 = random.randint(1, 100)
    if user_guess.lower() == "higher" or user_guess.lower() == "h":
        if random_integer2 > random_integer:
            console.print(f"[bold green]Congratulations! You guessed correctly. The second number was {random_integer2} which is higher than {random_integer}.[/bold green]")
        else:
            console.print(f"[bold red]Sorry! You guessed incorrectly. The second number was {random_integer2} which is not higher than {random_integer}.[/bold red]")


    elif user_guess.lower() == "lower" or user_guess.lower() == "l":
        if random_integer2 < random_integer:
            console.print(f"[bold green]Congratulations! You guessed correctly. The second number was {random_integer2} which is lower than {random_integer}.[/bold green]")
        else:
            console.print(f"[bold red]Sorry! You guessed incorrectly. The second number was {random_integer2} which is not lower than {random_integer}.[/bold red]")

    else:
        console.print("[bold red]Invalid input! Please enter 'higher', 'lower', or 'exit' to quit.[/bold red]")

    if user_guess.lower() in ("higher", "lower", "h", "l"):
        random_integer = random_integer2

