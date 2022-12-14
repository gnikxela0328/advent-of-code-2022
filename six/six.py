from data import message

buffer = []

for x in range(len(message)):

    # fill buffer
    if len(buffer) != 4:
        buffer.append(message[x])
    
    else:
        if len(set(buffer)) == 4:
            print(x)
            break
        else:
            buffer.pop(0)
            buffer.append(message[x])

buffer = []

for x in range(len(message)):

    # fill buffer
    if len(buffer) != 14:
        buffer.append(message[x])
    
    else:
        if len(set(buffer)) == 14:
            print(x)
            break
        else:
            buffer.pop(0)
            buffer.append(message[x])
