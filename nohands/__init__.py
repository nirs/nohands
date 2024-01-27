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

DELAY = 0.1
CHAR_DELAY = 0.075


def msg(s="", color=GREEN, prompt="$ ", wait=False, delay=DELAY, char_delay=CHAR_DELAY):
    for i in range(1, len(s)):
        print(f"{prompt}{color}{s[:i]}{RESET}", end="\r")
        time.sleep(char_delay)

    print(f"{prompt}{color}{s}{RESET}", end="" if wait else "\n")

    if wait:
        input()
    else:
        time.sleep(delay)


def run(*args, wait=False, delay=DELAY):
    show(args, wait=wait, delay=delay)
    subprocess.run(args)


def show(args, wait=False, delay=DELAY):
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

    msg(line, color=CYAN, prompt=prompt, wait=wait, delay=delay)
