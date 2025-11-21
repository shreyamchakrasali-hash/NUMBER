import sys

# Default values
num1 = 10
num2 = -5

# If command-line arguments are given, override the default values
if len(sys.argv) > 2:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
elif num1 < 0 and num2 < 0:
    print("Both numbers are negative.")
else:
    print("Numbers are mixed.")
