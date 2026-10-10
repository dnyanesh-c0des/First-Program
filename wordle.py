import random
import pyfiglet
from rich.console import Console

console = Console()
WORD_BANK = ["apple", "grape", "peach", "mango", "berry", "lemon", "melon", "plum", "cherry", "guava", "apple", "beach",
             "chief", "drive", "flame", "train", "world", "youth","plant", "storm", "cloud", "river", "ocean", "grass",
             "stone", "light","chair", "clock", "house", "shirt", "shoes", "table", "paper", "glass","bring", "catch", 
             "drink", "fight", "laugh", "match", "print", "share","smile", "speak", "stand", "think", "write", "sleep",
             "dance", "chase","build", "break", "count", "clean", "throw", "shine", "guide", "judge", "blind", "brave", 
             "clever", "cruel", "fresh", "great", "happy", "heavy","large", "lucky", "proud", "sharp", "smart", "sweet", 
             "total", "young","black", "white", "green", "brown", "short", "clear", "quick", "round","audio", "adieu", 
             "pique", "zilch", "quirk", "jazzy", "fuzzy", "proxy","vague", "fluff", "ghost", "karma", "lemur", "pizza", 
             "robot", "vivid"]

MAX_ATTEMPTS = 6


def show_title_and_rules():
    wordle_title = pyfiglet.figlet_format("WORDLE GAME", font="slant")
    print(wordle_title)

    console.print("[bold green]Welcome to the Wordle Game![/bold green]")
    console.print("[bold cyan]Rules of the Game:[/bold cyan]")
    console.print("[cyan]1. The computer will randomly select a 5-letter word from a predefined list.[/cyan]")
    console.print("[cyan]2. You have to guess the word within 6 attempts.[/cyan]")
    console.print("[cyan]3. After each guess, you will receive feedback on your guess.[/cyan]")
    console.print("[cyan]4. If a letter is in the correct position, it will be highlighted in green.[/cyan]")
    console.print("[cyan]5. If a letter is in the word but in the wrong position, it will be highlighted in yellow.[/cyan]")
    console.print("[cyan]6. If a letter is not in the word, it will be highlighted in gray.[/cyan]")
    console.print("[bold magenta]Let's start the game![/bold magenta]")


def get_feedback(secret_word, guess):
    feedback = ["gray"] * len(secret_word)
    remaining_letters = []

    for index, (secret_letter, guess_letter) in enumerate(zip(secret_word, guess)):
        if guess_letter == secret_letter:
            feedback[index] = "green"
        else:
            remaining_letters.append(secret_letter)

    for index, guess_letter in enumerate(guess):
        if feedback[index] == "green":
            continue
        if guess_letter in remaining_letters:
            feedback[index] = "yellow"
            remaining_letters.remove(guess_letter)

    return feedback


def show_guess(guess, feedback):
    colored_letters = []
    for letter, color in zip(guess, feedback):
        if color == "green":
            colored_letters.append(f"[bold black on green]{letter}[/bold black on green]")
        elif color == "yellow":
            colored_letters.append(f"[bold black on yellow]{letter}[/bold black on yellow]")
        else:
            colored_letters.append(f"[bold white on grey37]{letter}[/bold white on grey37]")

    console.print(" ".join(colored_letters))


def start_game():
    secret_word = random.choice(WORD_BANK)
    console.print(f"[bold]I have selected a 5-letter word. You have {MAX_ATTEMPTS} attempts.[/bold]")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            guess = console.input("[bold yellow]Enter your guess: [/bold yellow]").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                console.print("[bold red]Please enter a valid 5-letter word.[/bold red]")
                continue
            break

        feedback = get_feedback(secret_word, guess)
        show_guess(guess, feedback)

        if guess == secret_word:
            console.print(f"[bold green]Congratulations! You guessed the word in {attempt} attempt(s)![/bold green]")
            return

        console.print(f"[bold]Attempt {attempt}/{MAX_ATTEMPTS}[/bold]")

    console.print(f"[bold red]Game over! The word was [underline]{secret_word}[/underline].[/bold red]")


def main():
    show_title_and_rules()
    start_game()


if __name__ == "__main__":
    main()

