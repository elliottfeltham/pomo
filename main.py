import time
import sys
import os
from rich.console import Console
from InquirerPy import inquirer
from InquirerPy import get_style

# times
SHORT = 60 * 25
LONG = 60 * 50
REST = 60 * 5
BREAK = 60 * 30

# catppuccin mocha theme
RED = "#f38ba8"
GREEN = "#a6e3a1"
TEAL = "#94e2d5"
YELLOW = "#f9e2af"
PEACH = "#fab387"
LAVENDER = "#b4befe"

console = Console()
style = get_style(
    {
        "questionmark": PEACH,
        "pointer": GREEN,
        "answer": LAVENDER,
        "question": TEAL,
        "highlighted": YELLOW,
    },
    style_override=False,
)


def clear():
    os.system("tput reset")


def print_menu() -> None:
    clear()
    console.rule("[bold]" + f"[{GREEN}]POMO[/{GREEN}]", style=f"{RED}")
    print()

    pomo_choice = inquirer.select(
        "Select your mode:",
        choices=["25/5", "50/10", "Break", "Exit"],
        style=style,
        show_cursor=False,
    ).execute()
    print()
    return pomo_choice


def notify(message: str) -> None:
    title = "Pomo"
    # this can be the path to any mp3, wav, aiff etc.
    sound = "afplay /System/Library/Sounds/Ping.aiff &"
    os.system(sound)
    command = f'display dialog "{message}" with title "{title}" buttons {{"OK"}} default button "OK" giving up after 5'
    os.system(f"osascript -e '{command}' >/dev/null 2>&1")


def format_mm_ss(total_seconds: int) -> str:
    if total_seconds < 0:
        total_seconds = 0
    mins = total_seconds // 60
    secs = total_seconds % 60
    return f"{mins:02d}:{secs:02d}"


# This is now an ugly function because formatting a nice timer was harder
# than expected
def countdown(label: str, seconds: int) -> None:
    end = time.time() + seconds
    while True:
        remaining = int(end - time.time())
        if remaining <= 0:
            sys.stdout.write("\r")
            console.print(f"[{RED}]{label}: 00:00   [/{RED}]", end="")
            sys.stdout.flush()
            return
        sys.stdout.write("\r")
        console.print(f"{label}: {format_mm_ss(remaining)}   ", end="")
        sys.stdout.flush()
        time.sleep(1)


def run_work_then_break(work_secs: int, break_secs: int) -> None:
    # crtl+C will return to menu
    try:
        countdown("Lock in", work_secs)
        notify("Break time...")

        countdown("Break", break_secs)
        notify("Back to work...")
    except KeyboardInterrupt:
        return


def main() -> int:
    while True:
        try:
            choice = print_menu()
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        if choice == "25/5":
            run_work_then_break(SHORT, REST)
        elif choice == "50/10":
            run_work_then_break(LONG, REST * 2)
        elif choice == "Break":
            try:
                countdown("Break", BREAK)
                notify("Break Time is over...")
            except KeyboardInterrupt:
                return
        else:
            clear()
            sys.exit()
        console.print()


if __name__ == "__main__":
    main()
