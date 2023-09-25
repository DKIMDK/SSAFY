'''
김 프로는 수영장을 이용한다.
1년동안 각 달의 이용 계획을 수립하여 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 있다.

이용권 종류는 4종류
1. 1일 이용권
2. 1달 이용권 (매달 1일 시작)
3. 3달 이용권 (매달 1일 시작)
4. 1년 이용권 (1월 1일 시작)

입력
총 TC T
각 TC 첫 줄에는 이용권의 가격이 주어진다
둘째 줄에는 1~12월 이용 계획이 주어진다.

출력
#tc 최소비용

'''
def dfs(month, acc_cost):
    global ans

    if acc_cost > ans:
        return

    # 기저 조건
    if month > 12:
        ans = min(ans, acc_cost)
        return

    # 1일 이용권으로 모두 구입
    dfs(month + 1, acc_cost + (months[month] * cost_day))

    # 1달 이용권
    dfs(month + 1, acc_cost + cost_month)

    # 3달 이용권
    dfs(month + 3, acc_cost + cost_month3)

    # 1년 이용권
    dfs(month + 12, acc_cost + cost_year)

T = int(input())
for tc in range(1, T + 1):

    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())

    months = [0] + list(map(int, input().split()))
    ans = 100000000000

    dfs(1, 0)
    print(f'#{tc} {ans}')