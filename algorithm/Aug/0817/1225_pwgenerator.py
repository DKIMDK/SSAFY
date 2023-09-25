'''
8개의 숫자를 입력받는다
첫번째 숫자를 1 감소한 뒤 맨 뒤로 보낸다
그 다음 첫번째 숫자는 2 감소한 뒤 맨 뒤로..
5까지 감소 << 한 사이클

숫자가 0보다 작아지면 0으로 유지, 프로그램 종료

'''
def solution(arr):
    while True:
        for i in range(1, 5 + 1):
            k = arr.pop(0) - i
            # if k <= 0:
            #     k = 0
            #     arr.append(k)
            #     break
            arr.append(k)
            if arr[-1] <= 0:
                arr[-1] = 0
                return arr
    # return arr


for tc in range(1,10+1):
    int(input())
    arr = list(map(int, input().split()))
    arr = solution(arr)
    print(f'#{tc}', *arr)