s = raw_input()
l = ""
for i in range(len(s)):
    if i == 0 or s[i-1] == " ":
        l += s[i].upper()
    else:
        l += s[i]
        
print l