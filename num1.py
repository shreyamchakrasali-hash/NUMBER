import sys

if len(sys.argv) == 3:
    n1 = sys.argv[1]
    n2 = sys.argv[2]
else:
    n1 = "5"
    n2 = "-3"

# Convert n1
s1 = -1 if n1[0] == '-' else 1
v1 = 0
for c in n1[1:] if s1 == -1 else n1:
    v1 = v1 * 10 + (ord(c) - 48)
v1 *= s1

# Convert n2
s2 = -1 if n2[0] == '-' else 1
v2 = 0
for c in n2[1:] if s2 == -1 else n2:
    v2 = v2 * 10 + (ord(c) - 48)
v2 *= s2

# ------- SIMPLE MAIN PART --------
if v1 > 0 and v2 > 0:
    print("Both Positive")
elif v1 < 0 and v2 < 0:
    print("Both Negative")
else:
    print("Mixed")
# ---------------------------------
