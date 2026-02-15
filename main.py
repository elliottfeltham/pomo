import time
import sys
import os


SHORT = 60 * 25
LONG = 60 * 50
REST = 60 * 5
BREAK = 60 * 30


def print_menu() -> None:
    print("=== Pomo ===")
    print("1) 50/10")
    print("2) 25/5")
    print("3) 30s break")
    print("q) quit")
    print("> ", end="", flush=True)


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


def countdown(label: str, seconds: int) -> None:
    end = time.time() + seconds
    while True:
        remaining = int(end - time.time())
        if remaining <= 0:
            print(f"\r{label}: 00:00   ", end="", flush=True)
            return
        print(f"\r{label}: {format_mm_ss(remaining)}   ", end="", flush=True)
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
        print_menu()
        try:
            choice = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            sys.exit()

        if choice in {"q", "quit", "exit"}:
            sys.exit()

        if choice == "1":
            run_work_then_break(SHORT, REST)
        elif choice == "2":
            run_work_then_break(LONG, REST * 2)
        elif choice == "3":
            countdown("Break", BREAK)
            notify("Break Time is over...")
        else:
            print("Try again.")

        print()


if __name__ == "__main__":
    main()
