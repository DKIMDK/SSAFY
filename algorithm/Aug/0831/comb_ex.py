# ## 부분집합의 합이 0이 되는 모든 경우 출력
# #1. bit
# def subset(i, N):
#     if i == N:
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += arr[j]
#         if s == 0:
#             for j in range(N):
#                 if bit[j]:
#                     print(arr[j], end = ' ')
#             print()
#     else:
#         bit[i] = 1
#         subset(i+1, N)
#         bit[i] = 0
#         subset(i+1, N)
#     return
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bit = [0] * N
# subset(0, N)
#2.
def subset(i, N, s, c):         # 합이 0 -> 공집합의 문제, cnt
    if s == 0:
        return 1
    elif i == N:
        return 0
    else:
        if subset(i+1, N, s+arr[i], c+1):
            return 1
        if subset(i+1, N, s, c):
            return 1
        return 0

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
print(subset(0, N, 0, 0))