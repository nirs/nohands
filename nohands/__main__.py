# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
# SPDX-License-Identifier: MIT

import sys
import argparse

import nohands
from nohands import demo


def main():
    p = argparse.ArgumentParser("nh")
    p.add_argument("-r", "--reset", action="store_true", help="go to first step")
    p.add_argument("-p", "--previous", action="store_true", help="go to previous step")
    p.add_argument("-s", "--skip", action="store_true", help="skip current step")
    p.add_argument("--init", action="store_true", help="create a new demo in the current directory")
    args = p.parse_args()

    if args.init:
        init()
    elif args.reset:
        reset()
    elif args.previous:
        previous()
    elif args.skip:
        skip()
    else:
        run()


def init():
    demo.init()
    print(f"Created new demo in {demo.BASE}")
    sys.exit(0)


def reset():
    demo.reset()
    step = demo.step(0)
    print(f"Next: {step['name']}")
    sys.exit(0)


def previous():
    previous = max(0, demo.current() - 1)
    demo.advance(previous)
    step = demo.step(previous)
    print(f"Next: {step['name']}")
    sys.exit(0)


def skip():
    current = demo.current()
    step = demo.step(current + 1)
    if step is None:
        print(f"Next: [done]")
    else:
        demo.advance(current + 1)
        print(f"Next: {step['name']}")
    sys.exit(0)


def run():
    current = demo.current()
    step = demo.step(current)
    if step is None:
        sys.exit("[done]")

    demo.advance(current + 1)
    nohands.msg(step["name"])
    if "run" in step:
        try:
            nohands.run(*step["run"], delay=step["delay"])
        except KeyboardInterrupt:
            # Interrupting a command is not an error. Typical use case is to
            # run "watch command ..." and interrupt the command when needed.
            pass
