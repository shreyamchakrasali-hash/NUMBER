import sys

# Default values
default1 = 0
default2 = 0

if len(sys.argv) != 3:
    print("Insufficient arguments provided.")
    print("Usage: python pythoncal.py <Integer1> <Integer2>")
    print(f"Using default values: {default1}, {default2}")

    integer1 = default1
    integer2 = default2
else:
    integer1 = int(sys.argv[1])
    integer2 = int(sys.argv[2])

print(f"Integer1 {integer1} and Integer2 {integer2}")

# Check integer1
if integer1 > 0:
    print(f"{integer1} is a positive number")
elif integer1 < 0:
    print(f"{integer1} is a negative number")
else:
    print(f"{integer1} is neither negative nor positive")

# Check integer2
if integer2 > 0:
    print(f"{integer2} is a positive number")
elif integer2 < 0:
    print(f"{integer2} is a negative number")
else:
    print(f"{integer2} is neither negative nor positive")
