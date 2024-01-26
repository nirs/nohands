<!--
SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com>
SPDX-License-Identifier: MIT
-->

# Look ma no hands!

[![Available on PyPI](https://img.shields.io/pypi/v/nohands.svg)](https://pypi.python.org/pypi/nohands)
[![Downloads per month](https://img.shields.io/pypi/dm/nohands)](https://pypi.python.org/pypi/nohands)
[![MIT license](https://img.shields.io/pypi/l/nohands)](https://pypi.python.org/pypi/nohands)

A little library and command line tool for effortless demos.

## Example - fully scripted demo

When you have a short demo that can be fully scripted and requires no
interaction, you can scrip the entire demo in one python module.

[![asciicast](https://asciinema.org/a/633574.svg)](https://asciinema.org/a/633574)

See `example.py` for details.

## Example - interactive demo

When you need an interactive demo - run one command, discuss the command
and the output, then run the next command, you can create a demo yaml
and interact with the demo with the `nh` tool.

[![asciicast](https://asciinema.org/a/633578.svg)](https://asciinema.org/a/633578)

## Example - navigating an interactive demo

You can navigate in an interactive demo using the `--reset`, `--skip`,
and `--previous` options.

[![asciicast](https://asciinema.org/a/633581.svg)](https://asciinema.org/a/633581)

## License

This work is licensed under MIT license. See `LICENSES/MIT.txt` for more
info.
