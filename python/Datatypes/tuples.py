# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
m = map(int,raw_input().split())
t = tuple(m)
print hash(t)