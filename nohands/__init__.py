# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
# SPDX-License-Identifier: MIT

import subprocess
import time

__all__ = ["msg", "run", "GREEN", "CYAN", "YELLOW", "GREY"]
__version__ = "0.2.0"

GREY = "\033[38;5;250m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


def msg(s="", color=GREEN, delay=0.1, char_delay=0.075, prompt="$ "):
    for i in range(1, len(s)):
        print("{}{}{}{}".format(prompt, color, s[:i], RESET), end="\r")
        time.sleep(char_delay)
    print("{}{}{}{}".format(prompt, color, s, RESET), end="\n")
    time.sleep(delay)


def run(*args, delay=0.1):
    show(args, delay=delay)
    subprocess.run(args)


def show(args, delay=0.1):
    prompt = "$ "
    line = sep = ""

    for arg in args:
        if " " in arg:
            arg = "'" + arg + "'"
        if len(line) + len(arg) > 80:
            line += sep + "\\"
            msg(line, color=CYAN, prompt=prompt)
            prompt = "      "
            line = sep = ""
        line += sep + arg
        sep = " "

    msg(line, color=CYAN, prompt=prompt, delay=delay)
