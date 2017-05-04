#!/usr/bin/env python

import fileinput
import pocker

data = []
for inp in fileinput.input():
    data.append(inp.replace('\n', ''))

players = pocker.setup(data)
winner = pocker.announce_winner(pocker.play(players))
print(winner)
