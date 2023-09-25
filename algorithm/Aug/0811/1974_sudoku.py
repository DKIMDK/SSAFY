'''
스도쿠 검증
퍼즐은 모두 숫자로 채워진 상태로 주어진다
입력
첫줄에 테스트케이스 개수 T
9 줄에 걸쳐 9 개의 숫자 제시
출력
True 1 False 0
'''
def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 9+1):
            if cnt[k] == 0:
                return 0



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(sudoku(arr))
