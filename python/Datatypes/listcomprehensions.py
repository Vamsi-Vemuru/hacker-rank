x1 = int(raw_input())
x2 = int(raw_input())
x3 = int(raw_input())
n = int(raw_input())
li = [[xi,yi,zi] for xi in range(x1 + 1) for yi in range(x2 + 1) for zi in range(x3 + 1) if xi + yi + zi != n]
print li