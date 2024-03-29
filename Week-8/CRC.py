from random import randint


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def transmitter(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def receiver(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def encodeData(data, key=None):
    if key is None:
        key = ''
        for _ in range(randint(1, len(data)-1)):
            key += str(randint(0, 1))

    l_key = len(key)

    appended_data = data + '0' * (l_key - 1)
    remainder_t = transmitter(appended_data, key)

    print("Remainder:", remainder_t)

    codeword = data + remainder_t
    print("Codeword:", codeword)

    remainder_r = receiver(codeword, key)

    if remainder_r == "0" * (l_key - 1):
        print("Data received successfully")
    else:
        print("Error receiving data")


data = input("Enter data: ")
key = input("Enter generator: ")
# encodeData(data)  # without generator
encodeData(data, key)  # with generator
