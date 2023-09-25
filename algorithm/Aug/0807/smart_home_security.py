'''
AI의 발전으로 인해 세상의 많은 것이 편해졌다.
하지만 이로 인해 많은 것이 불편해진 것도 있다.
그 중 하나가 바로 사이버 범죄가 너무 많이 일어난다는 것이다.

사람들은 AI를 활용해 인터넷 상에서 개인정보 해킹 등 여러 방면에서 문제를 일으키고 있다.
그렇기 때문에 많은 웹사이트나 앱 등에서 '사람인가?'를 인증하기 위한 Captcha Code를
AI가 뚫을 수 없도록 발전시키고 있다.

코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.
[1] 랜덤으롤 N개 길이의 Sample이 주어진다.
[2] 그리고 K개 길이의 PassCode가 주어진다.
[3] 사용자는 Sample에서 PassCode를 '순차적으로' 만들 수 있는지를 검증해야 한다.

...

입력 예시
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

출력 예시
#1 1
#2 0

'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = input().split()
    passcode = input().split()

    # index = 0
    # result = False
    # for i in range(N):
    #     if passcode[index] == sample[i]:
    #         index += 1
    #     if index == K:
    #         result = True
    #         break
    #
    # print(f'#{tc} {result + 0}'
    #
    indexes = []
    result = 1

    for i in range(K):
        now = passcode[i]
        try:
            index = sample.index(now)
            sample = sample[index + 1:]
        except:
            result = 0
    print(f'#{tc} {result}')