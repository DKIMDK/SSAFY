# def solution(arr):
#     N = len(arr)
#     Min = float('inf')
#     result = []
#
#     def DFS(row, total, selected):
#         nonlocal Min, result
#
#         if row == N:
#             if total < Min:
#                 Min = total
#                 result = selected[:]
#             return
#
#         for i in range(N):
#             if i not in selected:  # 이미 선택된 열이 아닌지 확인
#                 selected.append(i)
#                 DFS(row + 1, total + arr[row][i], selected)
#                 selected.pop()
#
#     # 첫 번째 행을 시작으로 호출
#     for i in range(N):
#         DFS(1, arr[0][i], [i])
#
#     return sum([arr[i][result[i]] for i in range(N)])  # 선택된 열에 해당하는 값을 반환
import heapq

def solution(arr):
    N = len(arr)
    min_sum = float('inf')
    result = []

    def DFS(row, total, selected):
        nonlocal min_sum, result

        if total >= min_sum:  # 현재 합이 최소값보다 크면 탐색 중단
            return

        if row == N:
            min_sum = total
            result = selected[:]
            return

        for i in range(N):
            if i not in selected:
                new_total = total + arr[row][i]
                new_selected = selected + [i]
                DFS(row + 1, new_total, new_selected)

    for i in range(N):
        DFS(1, arr[0][i], [i])

    return sum([arr[i][result[i]] for i in range(N)])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solution(arr)
    print(f'#{tc} {ans}')