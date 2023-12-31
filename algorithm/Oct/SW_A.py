'''
코코는 아케이드 게임장에 친구와 함께 놀러갔다.
코코는 본인이 가장 좋아하는 풍선 사격 게임을 하려고 한다. 
게임은 아래와 같이 진행된다. 

① 숫자가 적힌 N개의 풍선들이 나란히 서 있다. 
② 참가자에게는 게임 총과 N개의 총알들이 주어진다. 
③ 참가자는 N개의 총알을 발사하여 풍선을 터트리면 아래에 설명한 방식으로 점수를 얻는다.
④ 풍선이 터지고 난 뒤 터지지 않은 풍선들은 일정한 간격을 가지도록 이동한다. 
⑤ 최종적으로 획득한 점수에 따라 경품을 받는다. 풍선을 터트릴 때 얻는 점수는 다음과 같이 계산된다. 

     ⓐ 점수는 0점부터 시작한다. 
     ⓑ 풍선이 터지면, 좌우로 이웃한 풍선에 적힌 두 숫자들의 곱으로 점수를 얻는다. 
     ⓒ 좌우로 한쪽만 이웃하는 풍선이 있는 경우, 이웃한 풍선에 적힌 숫자 만큼 점수를 얻는다.
     ⓓ 좌우로 이웃하는 풍선이 없는 경우, 터진 풍선에 적힌 숫자 만큼 점수를 얻는다. 
     ⓔ 어떤 풍선도 터트리지 못한 경우, 점수를 얻지 못한다. 

풍선 사격 게임에서 얻을 수 있는 최대 점수를 계산하는 프로그램을 작성하라.

[제약 사항] 
1. 풍선의 개수 N은 1부터 10까지의 정수이다. (1 ≤ N ≤ 10) 
2. 풍선에 적힌 숫자 Ki는 1부터 1000 이하의 정수이다. (1 ≤ Ki ≤ 1000, Ki는 좌로부터 i번째 풍선에 적힌 숫자) 
3. 풍선이 동시에 2개 이상 터지는 경우는 없다. 

입력
첫번째 줄에 test case의 개수 T (1 <= T <= 50) 가 공백주어진다. 다음 줄부터 각 test case에 대한 정보가 주어진다. 
각 test case의 첫번째 줄에는 N이 주어진다.
다음 줄에는 N개의 풍선의 점수에 대한 정보가 주어진다.
출력
각 test case에 대하여 "#"와 test case의 번호 (1번부터 시작)와 공백을 둔 후, 풍선 사격 게임에서 낼 수 있는 최고점을 출력한다. 
'''
'''
3 10 1 2 5

'''
def solution(balloons, point):
    if not balloons:
        return point
    elif len(balloons) == 1:
        point += balloons[0]
        balloons.pop()
    elif len(balloons) == 2:
            point += (balloons[1] * 2)
            balloons.pop()
            balloons.pop()

    else:
        max_i = 0
        max_score = balloons[1]
        for i in range(1, len(balloons) - 1):
            score = balloons[i-1] * balloons[i+1]
            if max_score < score:
                max_score = score
                max_i = i
        if max_score < balloons[-2]:
            max_score = balloons[-2]
            max_i = -1
        point += max_score
        del balloons[max_i]
    return solution(balloons, point)
            


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split()))
    point = 0
    answer = solution(balloons, point)
    print(f'#{tc} {answer}')






















