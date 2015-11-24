def last(a):
	return a[-1]

in1 = int(raw_input())
li = []
for i in range(in1):
	li1 = []
	li1.append(raw_input())
	li1.append(float(raw_input()))
	li.append(li1)
li = sorted(li, key=last)
lowest = li[0][1]
for i in li:
	if i[1] > lowest:
		second_lowest = i[1]
		break
sl = []
for i in li:
	if i[1] == second_lowest:
		sl.append(i[0])
for i in sorted(sl):
	print i