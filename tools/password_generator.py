import random
import string

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()


def password_generator() -> None:
    console.print(
        Panel(
            "[bold cyan]Password Generator[/bold cyan]\n[dim]Create secure random passwords[/dim]",
            border_style="cyan",
        )
    )

    try:
        length = IntPrompt.ask("[bold yellow]Password length[/bold yellow]", default=12)
        if length <= 0:
            console.print("[bold red][-] Length must be greater than 0.[/bold red]")
            input("\nPress Enter to return...")
            return

        use_digits = Prompt.ask(
            "[bold yellow]Include digits?[/bold yellow] (y/n)",
            choices=["y", "n", "Y", "N"],
            default="y",
        ).lower() == "y"

        use_symbols = Prompt.ask(
            "[bold yellow]Include symbols?[/bold yellow] (y/n)",
            choices=["y", "n", "Y", "N"],
            default="y",
        ).lower() == "y"

        chars = string.ascii_letters
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if not chars:
            console.print("[bold red][-] No character set selected.[/bold red]")
            input("\nPress Enter to return...")
            return

        with console.status("[bold green]Generating secure password...[/bold green]", spinner="dots"):
            password = "".join(random.choice(chars) for _ in range(length))

        console.print("\n[bold green][+] Password generated successfully:[/bold green]")
        console.print(
            Panel(
                Text(password, style="bold white"),
                border_style="green",
                title="Result",
            )
        )

    except ValueError:
        console.print("[bold red][-] Invalid input. Please enter a valid number.[/bold red]")
    except Exception as e:
        console.print(f"[bold red][-] Unexpected error: {e}[/bold red]")

    input("\nPress Enter to return...")