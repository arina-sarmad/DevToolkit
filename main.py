import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

# ایمپورت کردن ابزارها
from tools.password_generator import password_generator
from tools.calculator import calculator
from tools.hash_generator import hash_generator
from tools.qr_generator import qr_generator
from tools.json_formatter import json_formatter

console = Console()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    banner_text = """
 █▀▄ █▀▀ █ █ ▀█▀ █▀█ █▀█ █   █ █ █ ▀█▀
 █▄▀ ██▄ ▀▄▀  █  █▄█ █▄█ █▄▄ █▀▄ █  █ 
             [ DevToolkit v1.0.0 ]
    """
    # نمایش یک پنل بنفش‌رنگ و شیک دور بنر
    console.print(Panel(banner_text, style="bold cyan", border_style="bright_magenta",
                        subtitle="Developed with ❤️ for Developers"))


def main():
    while True:
        clear_screen()
        show_banner()

        # ساخت یک جدول شیک برای گزینه‌ها
        table = Table(show_header=True, header_style="bold yellow", border_style="blue")
        table.add_column("Key", style="dim", width=6, justify="center")
        table.add_column("Tool Name", min_width=30)
        table.add_column("Description", justify="left")

        table.add_row("1", "Password Generator", "Generate secure random passwords")
        table.add_row("2", "Smart Calculator", "Perform arithmetic operations safely")
        table.add_row("3", "Hash Generator", "Generate MD5 & SHA-256 hashes")
        table.add_row("4", "QR Code Generator", "Generate QR codes from URLs or Text")
        table.add_row("5", "JSON Formatter", "Validate and beautify JSON strings")
        table.add_row("0", "[bold red]Exit[/bold red]", "Close the application")

        console.print(table)
        console.print("\n")

        choice = Prompt.ask("[bold green]Select an option[/bold green]", choices=["0", "1", "2", "3", "4", "5"])

        if choice == '1':
            clear_screen()
            password_generator()
        elif choice == '2':
            clear_screen()
            calculator()
        elif choice == '3':
            clear_screen()
            hash_generator()
        elif choice == '4':
            clear_screen()
            qr_generator()
        elif choice == '5':
            clear_screen()
            json_formatter()
        elif choice == '0':
            console.print("\n[bold yellow]Thank you for using DevToolkit! Goodbye! 👋[/bold yellow]")
            break


if __name__ == "__main__":
    main()




