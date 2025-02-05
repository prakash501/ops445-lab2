#!/usr/bin/env python3

import sys  # Import sys module to handle command-line arguments

# Check if exactly 2 additional arguments are provided (total arguments should be 3, including script name)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()  # Exit the script if incorrect number of arguments

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument (Name)
age = sys.argv[2]  # Second argument (Age)

# Print the output in the required format
print(f"Hi {name}, you are {age} years old.")
