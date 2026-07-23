import os
import qrcode

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def qr_generator() -> None:
    console.print(
        Panel(
            "[bold magenta]QR Code Generator[/bold magenta]\n[dim]Convert text or URL into QR image[/dim]",
            border_style="magenta",
        )
    )

    data = Prompt.ask("[bold yellow]Enter text / URL[/bold yellow]").strip()

    if not data:
        console.print("[bold red][-] Input cannot be empty.[/bold red]")
        input("\nPress Enter to return...")
        return

    filename = Prompt.ask(
        "[bold yellow]Output filename[/bold yellow]",
        default="qr_code.png"
    ).strip()

    if not filename.lower().endswith(".png"):
        filename += ".png"

    output_dir = "outputs"
    output_path = os.path.join(output_dir, filename)

    try:
        with console.status("[bold green]Generating QR Code...[/bold green]", spinner="dots"):
            os.makedirs(output_dir, exist_ok=True)

            img = qrcode.make(data)
            img.save(output_path)

        console.print(
            Panel(
                f"[bold green][✔] QR Code generated successfully[/bold green]\n\n"
                f"[bold white]Saved to:[/bold white] [cyan]{output_path}[/cyan]",
                title="Done",
                border_style="green",
            )
        )

    except Exception as e:
        console.print(f"[bold red][-] Failed to generate QR Code: {e}[/bold red]")

    input("\nPress Enter to return...")

