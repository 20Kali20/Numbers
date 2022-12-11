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

for i in range(1, len(numm) + 1):
    j = -1 * i
    k = j - 1
    if numm[j] > num[j]:
        while num[k] == 0:
            num[k] = s
            k -= 1
        num[k] -= 1
        num[j] += s
    sub = num[j] - numm[j]
    number.append(rest[sub])
for i in range(len(numm) + 1, len(num) + 1):
    j = -1 * i
    number.append(rest[num[j]])

number.reverse()
print(''.join(number))