# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
# SPDX-License-Identifier: MIT

import os
import yaml

BASE = ".nh"
CURRENT = os.path.join(BASE, "current")
DEMO = os.path.join(BASE, "demo.yaml")

SAMPLE = f"""\
steps:
  - name: "## My awesome demo!"
    run: [tree, {BASE}]
  - name: "## The demo yaml"
    run: [cat, {DEMO}]
  - name: "## The current file"
    run: [cat, {CURRENT}]
  - name: "Created with https://github.com/nirs/nohands/"
options:
  delay: 0.5
"""

def init():
    os.makedirs(BASE, exist_ok=True)
    advance(0)
    if not os.path.exists(DEMO):
        with open(DEMO, "w") as f:
            f.write(SAMPLE)


def current():
    with open(CURRENT) as f:
       return int(f.readline())


def advance(n):
    with open(CURRENT, "w") as f:
        f.write(f"{n}\n")


def reset():
    advance(0)


def step(n):
    with open(DEMO) as f:
        demo = yaml.safe_load(f)
        try:
            step = demo["steps"][n]
        except IndexError:
            return None
        else:
            if "delay" not in step:
                step["delay"] = delay(demo)
            return step


def delay(demo):
    return demo.get("options", {}).get("delay", 0.1)
