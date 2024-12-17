import sys

def add(x, y):
    result = x + y
    return result

if len(sys.argv) < 3:
    print("Usage: python script_name.py <num1> <num2>")
    sys.exit(1)

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
res = add(n1, n2)
print(n1, "+", n2, "=", res)
