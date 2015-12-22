n = int(raw_input())
width = len(bin(n)[2:])
for i in range(1, n+1):
	print str(i).rjust(width),str(oct(i)[1:]).rjust(width),str(hex(i)[2:]).upper().rjust(width),str(bin(i)[2:]).rjust(width)