#!/usr/bin/env python3
# Author: Prakash Gautam
# Author ID: Your_seneca_id
# Date Created: 2025/02/04

import sys

# Assign timer value from the first command-line argument
timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
