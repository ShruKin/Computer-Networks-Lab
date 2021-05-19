import functools
import random


def parityGenerator(msg):
    binary_li = list(map(int, list(msg)))
    parity = functools.reduce(lambda a, b: a ^ b, binary_li)
    return parity


def parityChecker(msg):
    p = parityGenerator(msg)
    if p == 0:
        return True
    else:
        return False


def sender(msg_li):
    fill = max([len(i) for i in msg_li])
    msg_li = [list(i.zfill(fill)) for i in msg_li]

    mat = []
    for m in msg_li:
        binary_li = list(map(int, list(m)))
        binary_li.append(parityGenerator(binary_li))
        mat.append(binary_li)

    parity_line = []
    for c in range(fill):
        parity_line.append(parityGenerator([row[c] for row in mat]))

    parity_line.append(parityGenerator(parity_line))
    mat.append(parity_line)

    send = []
    for m in mat:
        send.append(''.join(list(map(str, m))))

    return send


def receiver(msg_li):
    data = []
    for m in msg_li[:-1]:
        data.append(m[:-1])

    mat = []
    for m in msg_li:
        binary_li = list(map(int, list(m)))
        if parityChecker(binary_li) == False:
            return False, data
        mat.append(binary_li)

    for c in range(max([len(i) for i in msg_li])):
        if parityChecker([row[c] for row in mat]) == False:
            return False, data

    return True, data


data = list(map(str, input('Enter space seperated data to send: ').split()))
msg_send = sender(data)
print("Data with parity:", str(msg_send))

p, msg_received = receiver(msg_send)

print()
if p:
    print('The transmission was ERROR-FREE!\nThe data received is: ' + str(msg_received))
else:
    print('There was an ERROR in the data received!\nThe data received is: ' + str(msg_received))
