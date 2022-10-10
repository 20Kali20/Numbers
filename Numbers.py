num = int(input('Enter number: '))

def binary(num):
    bin_num = ''
    number = []
    while num != 0:
        number.append(num % 2)
        num //= 2
    for n in range(len(number)):
        bin_num += str(number[-1])
        number.pop()
    return bin_num

def octal(num):
    oct_num = ''
    number = []
    while num != 0:
        number.append(num % 8)
        num //= 8
    for n in range(len(number)):
        oct_num += str(number[-1])
        number.pop()
    return oct_num

def hexadecimal(num):
    hex_num = ''
    number = []
    rest = ['A', 'B', 'C', 'D', 'E', 'F']
    while num != 0:
        if num % 16 > 9:
            number.append(rest[(num % 16) - 10])
        else:
            number.append(num % 16)
        num //= 16
    for n in range(len(number)):
        hex_num += str(number[-1])
        number.pop()
    return hex_num

print('Binary system: ', binary(num))
print('Octal system: ', octal(num))
print('Hexadecimal system: ', hexadecimal(num))