'''
첫 번째 줄부터 다섯 번째 줄까지 빙고판의 각 행의 숫자가 공백으로 구분되어 주어진다.
여섯 번째 줄부터 열 번째 줄까지 사회자가 부르는 숫자가 순서대로 각 줄에 5개씩 공백으로 구분되어 주어진다.
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 숫자가 중복 없이 사용된다.

출력
첫 번째 줄에 사회자가 어떤 숫자를 불렀을 때 3선 빙고가 완성되는지를 출력한다.
'''
# def bingo(table, call):
#     n = len(table)
#     bingo_count = 0
#     for i in call:
#         for y in range(n):
#             for x in range(n):
#                 if table[y][x] == i:
#                     table[y][x] = 0
#                     if sum(table[y]) == 0:
#                         bingo_count += 1
#                 for j in range(n):
#                     v_sum = []
#                     if sum(table[j][x]) == 0:
#                         bingo_count += 1
#                 for k in range(n):
#                     if sum(table[k][k]) == 0 or sum(table[k][n - 1 - k]):
#                         bingo_count += 1
#         if bingo_count == 3:
#             break
#     return i
#
# table = [list(map(int, input().split())) for _ in range(5)]
# call = [int(num) for _ in range(5) for num in input().split()]
#
# answer = bingo(table, call)
# print(answer)
board = [int(num) for _ in range(5) for num in input().split()]
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0

x_lst = [0] * 10
y_lst = [0] * 10
di_lst1 = [0] * 10
di_lst2 = [0] * 10

for n in call:

    a = board.index(n)

    x, y = a // 5, a % 5

    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x + y] += 1  # 우상좌하 대각선 칸 체크
    di_lst2[y - x + 4] += 1  # 좌상우하 대각선 칸 체크

    if x_lst[x] == 5:
        cnt += 1
    if y_lst[y] == 5:
        cnt += 1
    if di_lst1[x + y] == 5 or di_lst2[y - x + 4] == 5:
        cnt += 1

    if cnt == 3:
        print(n)
        break