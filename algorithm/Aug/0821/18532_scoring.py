'''

[제약사항]
3 <= N <= 30
2 <= M <= 40
정답 및 학생의 답안지로 입력되는 값은 1~5 사이의 정수이다.

입력
첫번째 줄에는 테스트 케이스의 개수 T가 주어진다.
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 학생의 수 N, 문제의 수 M이 공백으로 구분되어 주어진다.
각 테스트 케이스의 두번째 줄에는 M개의 문제에 대한 정답이 공백으로 구분되어 주어진다.
다음 N줄에 걸쳐, N명의 학생이 제출한 M개의 문제에 대한 답안지의 정보가 각 줄에 공백으로 구분되어 주어진다.

출력
각 테스트 케이 t에 대한 결과를 각 줄에 "#t" (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다.
'''
def solution(answer, submission):
    score = 0
    bonus = 0
    M = len(answer)
    for i in range(M):
        if answer[i] == submission[i]:
            score += 1 + bonus
            bonus += 1
        else:
            bonus = 0

    return score

T = int(input())
for tc in range(1, T+1):
    hs = 0
    ls = 56
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    for _ in range(N):
        submission = list(map(int, input().split()))
        score = solution(answer, submission)
        if hs < score:
            hs = score
        if ls > score:
            ls = score
    result = hs - ls
    print(f'#{tc} {result}')