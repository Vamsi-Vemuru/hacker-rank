no_of_cmd = input()
arr = []
for i in range(no_of_cmd):
    cmdEnt = raw_input()
    
    cmd = cmdEnt.split()
    
    if cmd[0] == 'insert':
        arr.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'append':
        arr.append(int(cmd[1]))
    elif cmd[0] == 'remove':
        arr.remove(int(cmd[1]))
    elif cmd[0] == 'pop':
        arr.pop()
    elif cmd[0] == 'index':
        option = cmd[1]
        print arr.index(int(option))
    elif cmd[0] == 'count':
        option = cmd[1]
        print arr.count(int(option))
    elif cmd[0] == 'sort':
        arr.sort()
    elif cmd[0] == 'reverse':
        arr.reverse()
    elif cmd[0] == 'print':
        print arr