'''
코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.
[1] 랜덤으로 N개 길이의 Sample이 주어진다.
[2] 그리고 K개 길이의 PassCode가 주어진다.
[3] 사용자는 Sample에서 PassCode를 "순차적으로" 만들 수 있는지를 검증해야 한다.

코코는 자신이 만든 생성기에 문제가 있는지 없는지 직접 QA 과정을 거치려고 한다.
Sample과 PassCode가 주어졌을때, Sample에서 PassCode를 만들 수 있는지 없는지를 판단하는 프로그램을 작성하라.

[제약사항]
5 <= N <= 300,000
3 <= K < N
입력
첫번째 줄에는 테스트 케이스의 개수 T가 주어진다.
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 Sample의 길이 N, PassCode의 길이 K가 주어진다.
각 테스트 케이스의 두번째 줄에는 N개 길이의 Sample이 공백으로 구분되어 주어진다.
각 테스트 케이스의 세번째 줄에는 K개 길이의 PassCode가 공백으로 구분되어 주어진다.
공백으로 주어지는 값은 0과 9사이의 정수이다.

2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

출력
#1 1
#2 0
'''
def solution(sample, passcode):
    while passcode:
        now = passcode.pop(0)
        for i in range(len(sample)):
            if sample[i] == now:
                sample = sample[i+1:]
                break
            if now not in sample:
                return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    ans = solution(sample, passcode)
    print(f'#{tc} {ans}')