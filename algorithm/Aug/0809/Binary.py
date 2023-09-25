def Binary(N):
    if N == 0: return '0'
    elif N == 1: return '1'
    else:
        return Binary(N// 2) + str(N % 2)

N = int(input())
print(Binary(N))