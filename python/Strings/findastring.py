inp1 = raw_input()
inp2 = raw_input()
occ = 0
for i in range(len(inp1)-len(inp2) + 1):
    if inp1[i:i+len(inp2)] == inp2:
        occ += 1
        
print occ