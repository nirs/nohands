# SPDX-FileCopyrightText: Nir Soffer <nirsof@gail.com>
# SPDX-License-Identifier: MIT

from nohands import *

run("clear")

msg()
msg("### How to use nohands ###", delay=3)
msg()
msg("Never make a typo again!")
msg("let the computer type for you")
msg("or run programs:")
msg()

run("ls", "-lh")

msg()
msg("Script complex demos without missing one argument")
msg("or forgetting important steps")
msg("in the right order")
msg()

run("git", "log", "--oneline")

msg()
msg("Keep your demos in source control")
msg()
msg("Look ma, no hands!", color=YELLOW)
msg()
