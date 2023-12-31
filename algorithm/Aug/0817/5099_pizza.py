"""
N = 3
arr = [7, 2, 6, 5, 3]
def solution(N, arr):
    # logic arr를 앞에서부터 N개만큼 돌면서 값을 2로 나눈 몫으로 변환
    # 값이 0이 된 index는 더 이상 조회하지 않음. 그 순서에 arr의 다음 index를 배정
    [7//2, 2, 6, 5, 3] #q:  1
    [3, 2//2, 6, 5, 3] #q:  2
    [3, 1, 6//2, 5, 3] #q:  3
    [3//2, 1, 3, 5, 3] #q:  1
    [1, 1//2, 3, 5, 3] #q:  2 -> 4
    [1, 0, 3//2, 5, 3] #q:  3
    [1//2, 0, 1, 5, 3] #q:  1 -> 5
    [0, 0, 1, 5//2, 3] #q:  4
    [0, 0, 1//2, 2, 3] #q:  3 -> end
    [0, 0, 0, 2, 3//2] #q:  5
    [0, 0, 0, 2//2, 1] #q:  4
    [0, 0, 0, 1, 1//2] #q:  5 -> end
    return ans # ans = 4

case2
N = 5
arr = [5, 9, 3, 9, 9, 2, 5, 8, 7, 1]
def solution(N, arr):
    2 9 3 9 9 2 5 8 7 1 #q: [1, 2, 3, 4, 5]
    2 4 3 9 9 2 5 8 7 1 #q: [2, 3, 4, 5, 1]
    2 4 1 9 9 2 5 8 7 1 #q: [3, 4, 5, 1, 2]
    2 4 1 4 9 2 5 8 7 1 #q: [4, 5, 1, 2, 3]
    2 4 1 4 4 2 5 8 7 1 #q: [5, 1, 2, 3, 4]
    1 4 1 4 4 2 5 8 7 1 #q: [1, 2, 3, 4, 5]
    1 2 1 4 4 2 5 8 7 1 #q: [2, 3, 4, 5, 1]
    1 2 0 4 4 2 5 8 7 1 #q: [3, 4, 5, 1, 2]
    1 2 0 2 4 2 5 8 7 1 #q: [4, 5, 1, 2, 6]
    1 2 0 2 2 2 5 8 7 1 #q: [5, 1, 2, 6, 4]
    0 2 0 2 2 2 5 8 7 1 #q: [1, 2, 6, 4, 5]
    0 1 0 2 2 2 5 8 7 1 #q: [2, 6, 4, 5, 7]
    0 1 0 2 2 1 5 8 7 1 #q: [6, 4, 5, 7, 2]
    0 1 0 1 2 1 5 8 7 1 #q: [4, 5, 7, 2, 6]
    0 1 0 1 1 1 5 8 7 1 #q: [5, 7, 2, 6, 4]
    0 1 0 1 1 1 2 8 7 1 #q: [7, 2, 6, 4, 5]
    0 0 0 1 1 1 2 8 7 1 #q: [2, 6, 4, 5, 7]
    0 0 0 1 1 0 2 8 7 1 #q: [6, 4, 5, 7, 8]
    0 0 0 0 1 0 2 8 7 1 #q: [4, 5, 7, 8, 9]
    0 0 0 0 0 0 2 8 7 1 #q: [5, 7, 8, 9, 10]
    0 0 0 0 0 0 1 8 7 1 #q: [7, 8, 9, 10]
    0 0 0 0 0 0 1 4 7 1 #q: [8, 9, 10, 7]
    0 0 0 0 0 0 1 4 3 1 #q: [9, 10, 7, 8]
    0 0 0 0 0 0 1 4 3 0 #q: [10, 7, 8, 9]
    0 0 0 0 0 0 0 4 3 0 #q: [7, 8, 9]
    0 0 0 0 0 0 0 2 3 0 #q: [8, 9]
    0 0 0 0 0 0 0 2 1 0 #q: [9, 8]
    0 0 0 0 0 0 0 1 1 0 #q: [8, 9]
    0 0 0 0 0 0 0 1 0 0 #q: [9, 8]
    return ans # ans = 8
"""


def solution(N, arr):
    next = N
    queue = [i for i in range(N)]
    while len(queue) != 1:
        now = queue.pop(0)
        arr[now] = arr[now] // 2
        if arr[now] > 0:
            queue.append(now)
        elif arr[now] == 0:
            if next < len(arr):
                queue.append(next)
                next += 1
            else:
                continue
    return queue.pop() + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = solution(N, arr)
    print(f'#{tc} {ans}')