n = int(raw_input())
avg = {}
for i in range(n):
	inp = raw_input().split()
	name = inp[0]
	marks = map(float,inp[1:])
	avg[name] = sum(marks)/float(len(marks))
query = raw_input()
print avg[query]