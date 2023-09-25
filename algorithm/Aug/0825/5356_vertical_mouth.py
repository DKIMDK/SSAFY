'''
5줄의 입력을 받아 세로 순으로 출력
'''

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    # print(arr)
    print(f'#{tc}', end=' ')
    for x in range(15):
        for y in range(5):         # 문자열 길이 최대 15
            try:
                print(arr[y][x], end='')

            except:
                continue
    print()
