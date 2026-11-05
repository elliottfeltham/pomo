# Pomo

A focused Pomodoro timer for the terminal, built with Python, Rich, and
InquirerPy. It provides 25/5 and 50/10 work cycles plus a standalone long-break
timer, with macOS sound and dialog notifications when a phase completes.

## Features

- Interactive terminal menu
- 25-minute and 50-minute focus modes
- Short and long break timers
- Keyboard interruption that safely returns to the menu
- Native macOS completion sound and timed dialog
- Installable `pomo` command through `pipx`

## Installation

Requirements: Python 3.10 or later and macOS for native notifications.

```bash
brew install pipx
pipx ensurepath
git clone https://github.com/elliottfeltham/pomo.git
cd pomo
pipx install .
```

For editable development installs, use `pipx install -e .`.

## Usage

```bash
pomo
```

Choose a timer mode with the arrow keys. Press `Ctrl+C` during a timer to
return to the menu, or at the menu to exit.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Limitations

- The application is designed for macOS; its sound and dialog commands are
  platform-specific.
- Sessions are not persisted and there is no historical productivity tracking.
- The terminal must remain active for the timer process to continue.
