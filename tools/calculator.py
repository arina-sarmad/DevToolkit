from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def calculator() -> None:
    console.print(
        Panel(
            "[bold yellow]Smart Calculator[/bold yellow]\n[dim]Basic arithmetic operations[/dim]",
            border_style="yellow",
        )
    )

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Operator", justify="center")
    table.add_column("Meaning", justify="center")
    table.add_row("+", "Addition")
    table.add_row("-", "Subtraction")
    table.add_row("*", "Multiplication")
    table.add_row("/", "Division")
    console.print(table)

    try:
        num1 = float(Prompt.ask("[bold cyan]Enter first number[/bold cyan]"))
        op = Prompt.ask("[bold cyan]Enter operator[/bold cyan]", choices=["+", "-", "*", "/"])
        num2 = float(Prompt.ask("[bold cyan]Enter second number[/bold cyan]"))

        with console.status("[bold green]Calculating...[/bold green]", spinner="dots"):
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    console.print("[bold red][-] Division by zero is not allowed.[/bold red]")
                    input("\nPress Enter to return...")
                    return
                result = num1 / num2

        console.print(
            Panel(
                f"[bold green]{num1} {op} {num2} = {result}[/bold green]",
                title="Result",
                border_style="green",
            )
        )

    except ValueError:
        console.print("[bold red][-] Invalid numeric input.[/bold red]")
    except Exception as e:
        console.print(f"[bold red][-] Unexpected error: {e}[/bold red]")

    input("\nPress Enter to return...")



