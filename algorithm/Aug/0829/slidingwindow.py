# 주로 리스트와 같은 시퀀스 타입에서 일정 크기의 '윈도우'를 정한다
# 그 윈도우를 데이터의 처음부터 끝까지 움직이면서 해결한다.

'''
n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할 때 최댓값 구하기
합이 가장 큰 구간의 값

input
10 2
3 -2 -4 -9 0 3 7 13 8 -3

output
21

'''
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 0

    for i in range(m):
        max_v += arr[i]
        Max = max_v
        start = 0
        end = m-1
    for i in range(n - m):
        max_v += arr[i+m]
        max_v -= arr[i]
        if max_v > Max:
            Max = max_v
            start = i+1
            end = i+m
    print(f'#{tc} {start} {end} {Max}')

# for i in range(n-1):
#     k = sum(arr[i:i+m])
#     if max_v < k:
#         max_v = k
# print(max_v)

