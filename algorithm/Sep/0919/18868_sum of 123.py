# solving club backtracking의 탑 low
# 정수 n을 '1', '2', '3', '+' 만을 이용하여 표현하는 가짓수를 구하고자 합니다.
# 만약 정수 3을 나타내는 방법은 총 4 가지 이며, 다음과 같습니다.

# 1 + 1 + 1
# 1 + 2
# 2 + 1
# 3
 

# 만약 정수 4를 나타내는 방법은 총 7 가지 이며, 다음과 같습니다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
 
# 정수 n이 주어졌을 때, n을 1, 2, 3, + 로 나타내는 방법의 수를 구하는 프로그램을 작성해 주세요.

# 입력
# 30이하의 자연수 n이 주어집니다.
 

# 출력
# n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력합니다.
# backtracking
# {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제

n = int(input())
arr = [1, 2, 3]
cnt = 0
path = [0] * 30
def backtracking(i):
    global cnt
    # 기저 조건 - n일 때 종료
    if sum(path) == n:
        cnt += 1
        return
    for num in arr:
        # 가지치기 - n보다 크면
        if sum(path) > n:
            continue
        # 들어가기 전 로직 - 경로저장
        path[i] = num
        # 다음 재귀 함수 호출
        backtracking(i + 1)
        # 돌아와서 할 로직 - 초기화
        path[i] = 0


backtracking(0)
print(cnt)