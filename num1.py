import sys

# Check if exactly 2 arguments are provided (besides the script name)
if len(sys.argv) != 3:
    print("Usage: python pythoncal.py <Integer1> <Integer2>")
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
