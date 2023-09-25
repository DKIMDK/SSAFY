def solution(deck, order):
    odd = []                                # 홀수 덱 (B)
    even = []                               # 짝수 덱 (C)
    bonus = 0                               # 보너스 점수
    point_board = [0] * 10                  # 각 참가자의 점수판, 최대 10명이므로 10개
    for card in deck:                       # A 덱을 돌면서 B,C에 카드 배분
        if card == '+':                     # +면 보너스 점수 추가
            bonus += 1
        else:                               # 숫자면
            now = bonus + int(card)         # 보너스와 현재 카드를 더해서
            if now % 2 == 0:                # 짝수면 C덱에 추가
                even.append(now)
            else:                           # 홀수면 B덱에 추가
                odd.append(now)

    for i in range(len(odd)):               # B 덱을 돌면서
        point_board[i % 10] += odd.pop(0)   # 각 참가자가 순서대로 점수를 얻음 (queue)

    for j in range(len(even)):              # C 덱을 돌면서
        point_board[j % 10] += even.pop()   # 각 참가자가 순서대로 점수를 얻음 (stack)


    return point_board[order - 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    deck = input().split()
    ans = solution(deck, M)
    print(f'#{tc} {ans}')