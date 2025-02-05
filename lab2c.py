#!/usr/bin/env python3

import sys  # Import sys module to handle command-line arguments

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument (Name)
age = int(sys.argv[2])  # Second argument (Age) converted to integer

# Print the output in the required format
print(f"Hi {name}, you are {age} years old.")
