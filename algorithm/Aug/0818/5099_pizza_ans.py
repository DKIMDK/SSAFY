T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split())) # 각 피자의 초기 치즈 양
    # 피자 인덱스(피자 번호), 치즈의 양을 저장할 리스트
    pizzas = [[i + 1, p] for i, p in enumerate(cheeses)]
    oven = pizzas[:N]   # 화덕에 처음 넣는 피자들
    remain = pizzas[N:]

    while len(oven) > 1:        # 화덕에 피자가 하나 남을때까지
        now = oven.pop(0)
        now[1] //= 2            # 치즈의 양을 반으로 줄이기
        if now[1] == 0:         # 치즈가 다 녹았으면
            if remain:          # 남은 피자가 있으면 화덕에 넣기
                oven.append(remain.pop(0))
        else:                   # 치즈가 다 안녹았으면
            oven.append(now)    # 다시 화덕에 넣기
    # 화덕에 남은 마지막 피자의 {번호} 출력
    print(f'#{tc} {oven[0][0]}')