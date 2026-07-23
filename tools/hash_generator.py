import hashlib

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def hash_generator() -> None:
    console.print(
        Panel(
            "[bold blue]Hash Generator[/bold blue]\n[dim]Generate MD5 / SHA1 / SHA256 hashes[/dim]",
            border_style="blue",
        )
    )

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Option", justify="center")
    table.add_column("Algorithm", justify="center")
    table.add_row("1", "MD5")
    table.add_row("2", "SHA1")
    table.add_row("3", "SHA256")
    console.print(table)

    text = Prompt.ask("[bold yellow]Enter text to hash[/bold yellow]")
    choice = Prompt.ask(
        "[bold yellow]Choose algorithm[/bold yellow]",
        choices=["1", "2", "3"],
        default="3",
    )

    try:
        with console.status("[bold green]Generating hash...[/bold green]", spinner="dots"):
            encoded = text.encode()

            if choice == "1":
                algo_name = "MD5"
                result = hashlib.md5(encoded).hexdigest()
            elif choice == "2":
                algo_name = "SHA1"
                result = hashlib.sha1(encoded).hexdigest()
            else:
                algo_name = "SHA256"
                result = hashlib.sha256(encoded).hexdigest()

        console.print(
            Panel(
                f"[bold white]Algorithm:[/bold white] [cyan]{algo_name}[/cyan]\n\n"
                f"[bold white]Hash:[/bold white]\n[green]{result}[/green]",
                title="Result",
                border_style="green",
            )
        )

    except Exception as e:
        console.print(f"[bold red][-] Unexpected error: {e}[/bold red]")

    input("\nPress Enter to return...")
