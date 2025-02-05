#!/usr/bin/env python3
# Author: Prakash Gautam
# Author ID: Your_seneca_id
# Date Created: 2025/02/04

import sys

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
