# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
# SPDX-License-Identifier: MIT

import os
import yaml

import nohands

BASE = ".nh"
CURRENT = os.path.join(BASE, "current")
DEMO = os.path.join(BASE, "demo.yaml")

SAMPLE = f"""---
steps:
  - name: "Welcome to nohands!"
    run: [nh, --help]
  - name: "The .nh directory"
    run: [tree, .nh]
  - name: "The demo yaml"
    run: [cat, .nh/demo.yaml]
  - name: "Watching a program"
    run: [watch, date]
  - name: "That's all, folks!"
options:
  delay: 0.5
"""


def init():
    os.makedirs(BASE, exist_ok=True)
    if not os.path.exists(DEMO):
        with open(DEMO, "w") as f:
            f.write(SAMPLE)


def load():
    with open(DEMO) as f:
        return yaml.safe_load(f)


def option(doc, name, default=None):
    return doc.get("options", {}).get(name, default)
