# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
# SPDX-License-Identifier: MIT

import argparse
import contextlib
import curses
import curses.ascii as ascii
import subprocess
import sys
import time

from nohands import demo

COMMENT = 1
COMMAND = 2

DESCRIPTION = """
run efortless demos!

keys:
  space         go forward
  right,left    go forward or backward
  up,down       show menu
  enter         select menu item

builtins commands:
  watch         execute a program periodically, showing output
"""

def main():
    p = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--init",
        action="store_true",
        help="create a new demo in the current directory",
    )
    args = p.parse_args()

    if args.init:
        init()

    try:
        curses.wrapper(run)
    except KeyboardInterrupt:
        pass


def init():
    demo.init()
    print(f"Created new demo in {demo.BASE}")
    sys.exit(0)


def run(stdscr):
    if curses.has_colors():
        curses.use_default_colors()
        curses.init_pair(COMMENT, curses.COLOR_GREEN, -1)
        curses.init_pair(COMMAND, curses.COLOR_CYAN, -1)

    doc = demo.load()
    last = len(doc["steps"]) - 1
    current = 0

    while current <= last:
        play_step(doc, stdscr, current)
        current = next_step(doc, stdscr, current, last)

    show_about(stdscr)


def play_step(doc, win, n):
    step = doc["steps"][n]
    if "out" in step:
        show_step(step, win)
    else:
        build_step(doc, step, win)


def show_step(step, win):
    win.clear()
    for text, attr in step["out"]:
        win.addstr(text, attr)
    win.refresh()


def build_step(doc, step, win):
    win.clear()
    step["out"] = []
    add_prompt(step, win)
    type_comment(doc, step, win)
    if "run" in step:
        add_prompt(step, win)
        type_command(doc, step, win)
        run_step(step, win)


def add_prompt(step, win):
    text = "$ "
    step["out"].append((text, 0))
    win.addstr(text)
    win.refresh()


def type_comment(doc, step, win):
    text = "# " + step["name"] + "\n"
    attr = curses.color_pair(COMMENT) | curses.A_BOLD
    step["out"].append((text, attr))
    type_text(win, text, attr, delay=demo.option(doc, "delay"))


def type_command(doc, step, win):
    text = " ".join(step["run"]) + "\n"
    attr = curses.color_pair(COMMAND) | curses.A_BOLD
    step["out"].append((text, attr))
    type_text(win, text, attr, delay=demo.option(doc, "delay"))


def type_text(win, text, attr, wpm=120, delay=0.5):
    char_delay = 60 / wpm / 5
    for c in text:
        win.echochar(c, attr)
        time.sleep(char_delay)
    time.sleep(delay)


def show_about(win):
    text = "Created with https://github.com/nirs/nohands"
    height, width = win.getmaxyx()
    y = height // 2
    x = width // 2 - len(text) // 2
    curses.curs_set(0)
    win.clear()
    win.addstr(y, x, text, curses.A_BOLD)
    win.refresh()
    win.timeout(3000)
    win.getch()


def next_step(doc, win, current, last):
    while True:
        c = win.getch()
        if c == ascii.SP or c == curses.KEY_RIGHT:
            return current + 1
        if c == curses.KEY_LEFT:
            return max(current - 1, 0)
        if c == curses.KEY_UP:
            return select_step(doc, win, max(current - 1, 0), last)
        if c == curses.KEY_DOWN:
            return select_step(doc, win, min(current + 1, last), last)


def select_step(doc, win, current, last):
    saved_curs = curses.curs_set(0)
    while True:
        show_menu(doc, win, current)
        c = win.getch()
        if c == curses.KEY_UP:
            current = max(current - 1, 0)
        elif c == curses.KEY_DOWN:
            current = min(current + 1, last)
        elif c in (curses.KEY_ENTER, ascii.NL, ascii.CR):
            curses.curs_set(saved_curs)
            return current


def show_menu(doc, win, current):
    win.clear()

    height, width = win.getmaxyx()
    for i, step in enumerate(doc["steps"]):
        y = height // 2 - len(doc["steps"]) // 2 + i
        x = width // 2 - len(step["name"]) // 2

        attr = 0 if "out" in step else curses.A_BOLD
        if i == current:
            attr |= curses.A_REVERSE

        win.addstr(y, x, step["name"], curses.color_pair(COMMENT) | attr)

    win.refresh()


def run_step(step, win):
    command = step["run"]
    if command[0] == "watch":
        out = watch_command(win, command[1:])
    else:
        out = run_command(win, command)
    step["out"].extend(out)


def watch_command(win, command):
    cmdwin = win.subwin(*curses.getsyx())
    win.timeout(2000)
    while True:
        cmdwin.clear()
        out = run_command(cmdwin, command)
        c = win.getch()
        if c != -1:
            curses.ungetch(c)
            win.timeout(-1)
            return out


def run_command(win, command):
    cp = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    out = []

    for line in cp.stdout.decode().splitlines(True):
        out.append((line, 0))
        win.addstr(line)
        win.refresh()

    for line in cp.stderr.decode().splitlines(True):
        out.append((line, 0))
        win.addstr(line)
        win.refresh()

    return out
