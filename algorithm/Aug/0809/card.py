'''
다섯 종류의 카드를 입력 받습니다 ('0'~ '9')
다량으로 쌓여있습니다.
다섯 종류의 숫자 카드에서 4장을 뽑으려고 합니다.
뽑을 때마다 전에 뽑았던 카드번호와 간격이 3이하로 차이나는 중복순열이 몇가지인지 출력하세요
재귀호출을 이용해서

ex) 카드 종류가 1/2/3/4/5 일 때
1111: OK
1112: OK
...
1115: NO
...
nocount: 1251, 5123 등..
총 497가지

힌트
path[level-1]과 path[level]의 절대값이 3차이가 나는지 확인

'''
# def sol(arr):
#     count = len(arr)**4
#     for i in arr:
#         for j in arr:
#             for k in arr:
#                 for l in arr:
#                     path = [i, j, k, l]
#                     for level in range(1, len(path)):
#                         if abs(int(path[level - 1]) - int(path[level])) > 3:
#                             count -= 1
#                             break
#     return count
#
#
arr = ['1', '2', '3', '4', '5']
# print(sol(arr))
#
#
def recursive_sol(arr,
                  level=0,
                  prev_value=None):
    if level == 4:
        return 1

    count = 0
    for i in arr:
        if prev_value is None or abs(int(prev_value) - int(i)) <= 3:
            count += recursive_sol(arr, level + 1, i)

    return count


print(recursive_sol(arr))
# path = [0]*4
# card = list(input())
# cnt = 0
# def card_cnt(level): #level은 현재 뽑은 카드의 수
#     global cnt
#     # 4장의 카드를 뽑았으면 경우의 수 증가
#     if level == 4:
#         cnt += 1
#         return
#     for i in range(5):
#         path[level] = card[i]
#         valid = True
#
#         for j in range(level):
#             if (level and int(path[level]) - int(path[level -1]) >= 4) or (level and int(path[level-1]) - int(path[level]) >= 4):
#                 valid = False
#                 break
#         if valid:
#             card_cnt(level+1)
# card_cnt(0)
#
# print(cnt)