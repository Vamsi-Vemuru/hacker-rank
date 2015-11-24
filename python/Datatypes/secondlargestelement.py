n = int(raw_input())
arr = raw_input().split()
for i in range(n):
	arr[i] = int(arr[i])
arr = sorted(arr)
largest = arr[-1]
for i in reversed(arr):
	if i < largest:
		print i
		break