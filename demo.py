# Copyright (C) 2020 Nir Soffer <nirsof@gmail.com>
# This program is free software; see LICENCE for more details.

import subprocess
import time

__all__ = ["msg", "run", "GREEN", "CYAN", "YELLOW"]

GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


def msg(s="", color=GREEN, delay=1, char_delay=0.025, prompt="$ "):
    for i in range(1, len(s)):
        print("{}{}{}{}".format(prompt, color, s[:i], RESET), end="\r")
        time.sleep(char_delay)
    print("{}{}{}{}".format(prompt, color, s, RESET), end="\n")
    time.sleep(delay)


def run(*args):
    show(args)
    subprocess.run(args)


def show(args):
    prompt = "$ "
    line = sep = ""

    for arg in args:
        if len(line) + len(arg) > 80:
            line += sep + "\\"
            msg(line, color=CYAN, prompt=prompt, delay=0.5)
            prompt = "> "
            line = sep = ""
        line += sep + arg
        sep = " "

    msg(line, color=CYAN, prompt=prompt)
