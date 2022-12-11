pre_num = input('Enter  first number: ')
pre_numm = input('Enter second number: ')
s = int(input(''))

number = []
num = []
numm = []

rest = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for n in range(len(pre_num)):
    ind = rest.index(pre_num[n])
    num.append(ind)

for p in range(len(pre_numm)):
    ind = rest.index(pre_numm[p])
    numm.append(ind)

def add(num, numm, s, rest):
    for i in range(1, len(numm) + 1):
        j = -1 * i
        ad = num[j] + numm[j]
        if ad > s:
            num[j - 1] += ad//s
            ad -= s
        number.append(rest[ad])
    for i in range(len(numm) + 1, len(num) + 1):
        j = -1 * i
        number.append(rest[num[j]])

    number.reverse()
    return ''.join(number)

print(add(num, numm, s, rest))