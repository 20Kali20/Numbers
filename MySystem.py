num = int(input('Enter number: '))
s = int(input('Enter number between 1 and 35: '))

def system(num, s):
    sys_num = ''
    number = []
    rest = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while num != 0:
        number.append(rest[num % s])
        num //= s
    number.reverse()
    sys_num = ''.join(number)
    return sys_num

print(system(num, s))