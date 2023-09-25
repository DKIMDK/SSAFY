'''
Ugly Number는 숫자 2, 3, 5 를 사용하여 만들어 낼 수 있는 수를 뜻합니다.
예외로 숫자 1은 첫 번째 Ugly Number입니다.

Ugly Number들을 순서대로 나열해보면 다음과 같습니다.
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...

a, b, c ... 등 n 개의 수를 입력 받고,  a, b, c ... 번째 Ugly Number를 찾아 출력해 주세요.
만약 1 9 10 을 입력 받았다면, 출력 결과는 1 10 12 입니다.

입력
첫 번째 줄에 질의의 개수 Q가 입력됩니다. ( 1 <= Q <= 10,000)
각 질의 별로 K 가 입력되고 해당 K 번째 Ugly number 를 구해주시면 됩니다.
두 번째 줄에  "K번째"에 해당하는 양의 정수 Q개를 입력 받습니다. ( 1 <= K <= 1,500)

출력
각 질의에 해당하는 Ugly number를 출력해주세요.

'''
def solution(n):
    result = [0, 1]
    while True:
        last = result[-1]
        if len(result) - 1 == n:
            return result

        tmp = []
        for r in result:
            for t in r*2, r*3, r*5:
                if t > last:
                    tmp.append(t)

        result.append(min(tmp))


Q = int(input())
number = list(map(int, input().split()))
n = max(number)
tree = solution(n)
for num in number:
    print(tree[num], end=' ')