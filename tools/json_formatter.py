import json

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

console = Console()


def json_formatter() -> None:
    console.print(
        Panel(
            "[bold cyan]JSON Formatter[/bold cyan]\n[dim]Validate and pretty-print JSON[/dim]",
            border_style="cyan",
        )
    )

    json_str = Prompt.ask("[bold yellow]Enter JSON string[/bold yellow]")

    try:
        with console.status("[bold green]Formatting JSON...[/bold green]", spinner="dots"):
            data = json.loads(json_str)
            pretty_json = json.dumps(data, indent=4, ensure_ascii=False)

        console.print("[bold green][+] JSON is valid.[/bold green]\n")
        console.print(
            Panel(
                Syntax(pretty_json, "json", theme="monokai", line_numbers=True),
                title="Formatted JSON",
                border_style="green",
            )
        )

    except json.JSONDecodeError as e:
        console.print("[bold red][-] Invalid JSON.[/bold red]")
        console.print(f"[red]Details:[/red] {e}")
    except Exception as e:
        console.print(f"[bold red][-] Unexpected error: {e}[/bold red]")

    input("\nPress Enter to return...")


