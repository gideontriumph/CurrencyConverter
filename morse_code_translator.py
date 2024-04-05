"""
    Name: morse_code_translator.py
    Author: Triumph Ogbonnia
    Created: 4/4/24
    Purpose: Convert user input to morse code.
"""

from rich import print
from rich.console import Console
from rich.panel import Panel

# Initialize rich console
console = Console()

def main():
    # Define a dictionary containing morse code symbols for each letter
    symbols = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }

    console.print(
        Panel.fit(
            " ----    Morse Code Converter   ---- ",
            style="bold blue",
            subtitle="By Triumph Ogbonnia"
        )
    )
    # Ask the user to input a word or sentence to convert to morse code
    ask = console.input("[bold blue]\nType a word or sentence to convert to morse >> [/bold blue]")

    length = len(ask)
    output = ""

    # Convert each character in the input to morse code
    for i in range(length):
        if ask[i] in symbols.keys():
            output = output + " " + symbols.get(ask[i])

    # Print the resulting morse code
    print("[bold blue]\nMorse Code >> [/bold blue]")
    print(output)

# Initialize conversion
main()

# Ask the user if they want to run the code again
while True:
    run_again = console.input("[bold blue]\nWould you like to run the code again? (yes/no) >> [/bold blue]").lower()
    if run_again == "yes":
        main()
    elif run_again == "no":
        print("[bold cyan]Shutting down. . .[/bold cyan]")
        break
    else:
        print("[bold red]\n[+] Invalid input! Please enter 'yes' or 'no'[/bold red]")