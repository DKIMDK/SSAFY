# devide and conquer
def f1(base, exponent):
    global cnt1

    if base == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= base
        cnt1 += 1
    return result

def f2(base, exponent):
    global cnt2

    if exponent == 0 or base == 0:
        return 1
    if exponent % 2:
        result = f2(base, (exponent - 1) // 2)
        cnt2 += 1
        return result * result * base
    else:
        result = f2(base, exponent // 2)
        cnt2 += 1
        return result * result
cnt1 = 0
cnt2 = 0
print(f1(2, 20), cnt1)
print(f2(2, 20), cnt2)