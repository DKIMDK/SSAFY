N, M = map(int, input().split())


# arr = [i for i in range(1, 6 + 1)]
# path = [0] * N
# used = [0] * 7
# def backtracking(cnt):
#     # 기저 조건 - 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         print(*path)
#         return
    
   
#     for num in arr: 
#         if M == 3:
#             if num not in path:
#                 continue
#             # 들어가기 전 로직 - 경로저장
#             path[cnt] = num
#             # 다음 재귀 함수 호출
#             backtracking(cnt + 1)
#             # 돌아와서 할 로직 - 초기화
#             path[cnt] = 0

# backtracking(0)

path = [0] * 10
def printpath(level):
    print(' '.join(map(str, path[:level])))

def roll1(level):
    if level == N:
        printpath(level)
        return
    
    for i in range(1, 6 + 1):
        path[level] = i

        roll1(level + 1)

        path[level] = 0

def roll2(level):
    if level == N:
        printpath(level)
        return
    
    for i in range(1, 6 + 1):
        if level > 0 and i < path[level -1]:
            continue

        path[level] = i

        roll2(level + 1)

        path[level] = 0

used = [0] * 10

def roll3(level):
    if level == N:
        printpath(level)
        return
    
    for i in range(1, 6 + 1):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = i

        roll3(level + 1)

        used[i] = 0
        path[level] = 0

if M == 1:
    roll1(0)
elif M == 2:
    roll2(0)
elif M == 3:
    roll3(0)