T = int(input())
for tc in range(1, T + 1):
    num, c = input().split()
    c = int(c)
    now = set([num])
    next = set()
    for _ in range(c):
        while now:
            s = now.pop()
            s = list(s)
            # 숫자판의 모든 자리를 서로 교환
            for i in range(len(num) - 1):
                for j in range(i + 1, len(num)):
                    # 두 자리를 서로 교환
                    s[i], s[j] = s[j], s[i]
                    # 교환한 결과를 next 집합에 추가
                    next.add(''.join(s))
                    # 다시 원래 자리로 돌려놓기
                    s[i], s[j] = s[j], s[i]
        now, next = next, now # 현재 집합과 next 집합 교환
    result = max(map(int, now))
    print(f'#{tc} {result}')