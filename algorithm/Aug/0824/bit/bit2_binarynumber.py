bit = [0] * 8
a = 149
i = 7
while a > 0:
    bit[i] = a % 2
    a //= 2
    i -= 1
print(''.join(map(str, bit)))