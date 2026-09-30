import math
import rich
import pyfiglet


from rich.console import Console
console=Console()

from rich.progress import track
import time

calculator_title = pyfiglet.figlet_format("CALCULATOR", font="slant")

print(calculator_title)
console.log("[italic][bold green]Welcome to the Calculator![/bold green][/italic]")
console.print("Select operation:")
console.print("[cyan]1. Add [/cyan]") 
console.print("[cyan]2. Subtract [/cyan]")
console.print("[cyan]3. Multiply [/cyan]")
console.print("[cyan]4. Divide [/cyan]")
console.print("[cyan]5. Factorial [/cyan]")
console.print("[cyan]6. Square [/cyan]")
console.print("[cyan]7. Square Root [/cyan]")
console.print("[cyan]8. Power [/cyan]")
console.print("[cyan]9. Logarithm [/cyan]")
console.print("[cyan]10. Exit [/cyan]")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")
    for step in track(range(100), description="Processing..."):
        time.sleep(0.02)  # Simulate work

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice in ('5', '6','7','8','9'):
        num3 = int(input("Enter a number : "))

        if choice == '1':
            console.print(f"[bold orange]{num1} + {num2} = {num1 + num2} [/bold orange]")

        elif choice == '2':
            console.print(f"[bold orange]{num1} - {num2} = {num1 - num2} [/bold orange]")

        elif choice == '3':
            console.print(f"[bold orange]{num1} * {num2} = {num1 * num2} [/bold orange]")

        elif choice == '4':
            if num2 != 0:
                console.print(f"[bold orange]{num1} / {num2} = {num1 / num2} [/bold orange] ")
            else:
                console.print("[bold red]Error! Division by zero.[/bold red]")

        elif choice == '5':
            factorial = 1
            for i in range(1, num3+1):
                factorial = factorial * i
            console.print(f"[bold orange]The factorial of {num3} is {factorial}[/bold orange]")

        elif choice == '6':
            console.print(f"[bold orange]The square of {num3} is {num3 ** 2}[/bold orange]")

        elif choice == '7':
            if num3 >= 0:
                console.print(f"[bold orange]The square root of {num3} is {num3 ** 0.5}[/bold orange]")
            else:
                console.print("[bold red]Error! Cannot compute square root of a negative number.[/bold red]")

        elif choice == '8':
            exponent = int(input("Enter the exponent: "))
            console.print(f"[bold orange]{num3} raised to the power of {exponent} is {num3 ** exponent}[/bold orange]")

        elif choice == '9':
            if num3 > 0:
                console.print(f"[bold orange]The logarithm of {num3} is {math.log(num3)}[/bold orange]")
            else:
                console.print("[bold red]Error! Logarithm undefined for non-positive numbers.[/bold red]")

    elif choice == '10':
        console.print("[bold blue]Exiting the calculator. Goodbye! . Visit Again!![/bold blue]")
        break

    else:
        console.print("[bold red]Invalid Input[/bold red]")