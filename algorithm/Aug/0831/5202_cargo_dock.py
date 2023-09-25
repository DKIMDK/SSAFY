'''
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고,
다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.

1<=N<=100, 0<=s<24, 0 ＜ e ＜= 24
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cargos = []
    for _ in range(N):
        start, end = map(int, input().split())
        cargos.append((start, end))

    cargos.sort(key=lambda x: x[1])

    count = 1
    end_time = cargos[0][1]

    for i in range(1, N):
        if cargos[i][0] >= end_time:
            count += 1
            end_time = cargos[i][1]

    print(f'#{tc} {count}')