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


def sender(msg):
    return msg + str(parityGenerator(msg))


def receiver(msg):
    return parityChecker(msg), msg[:-1]


data = input('Enter data to send: ')
msg_send = sender(data)
print("Data with parity:", msg_send)

p, msg_received = receiver(msg_send)

print()
if p:
    print('The transmission was ERROR-FREE!\nThe data received is: ' + msg_received)
else:
    print('There was an ERROR in the data received!\nThe data received is: ' + msg_received)
