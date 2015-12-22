inp = raw_input()
inp2 = raw_input().split()
inp2[0] = int(inp2[0])
op = inp[:inp2[0]] + inp2[1] + inp[inp2[0] + 1:]
print op