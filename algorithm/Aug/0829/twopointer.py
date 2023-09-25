# 주로 리스트와 같은 시퀀스 타입에서 두 개의 포인터를 사용하여 문제를 풀이하는 방법
'''
1부터 10000 사이의 n개의 자연수 중에서 연속된 숫자를 더했을 때 합이 m이 되는 경우의 수를 구하라
(구간의 크기가 정해지지 않았음 -> 투포인터)

input
10 5
1 2 3 4 2 5 3 1 1 2

output
3
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt, total = 0, 0
high, low = 0, 0
while True:
    if total >= m or high == n: # 합이 타겟보다 크거나 같다면(범위좁히기)
        total -= arr[low]
        low += 1
    elif total < m:             # 합이 타겟보다 작다면(범위 넓히기)
        total += arr[high]
        high += 1
    if total == m:
        cnt += 1
    if low == n:
        break
print(cnt)

# for i in range(n-1):
#     for j in range(i, n):
#         if total(arr[i:j]) == 5:
#             cnt += 1
# print(cnt)