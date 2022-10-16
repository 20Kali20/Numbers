num = int(input('Enter number: '))

def binary(num):
    bin_num = ''
    number = []
    while num != 0:
        number.append(str(num % 2))
        num //= 2
    number.reverse()
    bin_num = ''.join(number)
    return bin_num

def octal(num):
    oct_num = ''
    number = []
    while num != 0:
        number.append(str(num % 8))
        num //= 8
    number.reverse()
    oct_num = ''.join(number)
    return oct_num

def hexadecimal(num):
    hex_num = ''
    number = []
    rest = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while num != 0:
        number.append(rest[num % 16])
        num //= 16
    number.reverse()
    hex_num = ''.join(number)
    return hex_num

print('Binary system: ', binary(num))
print('Octal system: ', octal(num))
print('Hexadecimal system: ', hexadecimal(num))