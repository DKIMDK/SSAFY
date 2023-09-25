'''
세부조건
1. 괄호는 없습니다.
2. 첫 번째 수는 양수 또는 음수가 될 수 있습니다.
3. +와 - 이외 문자는 입력되지 않습니다.
4. 띄어쓰기 없이 입력이 됩니다.
5. 문자열 길이 최대값: 1000
6. 최종 결과는 음수가 될 수 있습니다.
7. 첫 번째 수가 양수라면 +는 생략

입력:
첫 번째 줄에 다항식에 해당하는 '문자열'이 주어집니다.

출력:
다항식을 연산한 결과를 출력합니다.

입력 예시:
100+100-50+30

출력 예시:
180
'''

# 덧셈 기호를 기준으로 분리
ex = input()
if ex[0] == '-':
    ex = '0' + ex
word = ex.split('+')
ans = 0
for w in word:
    # 뺄셈 기호를 기준으로 분리
    w = w.split('-')
    # 첫 요소는 더하기
    inner_ans = int(w[0])
    # 나머지는 빼기
    for i in range(1, len(w)):
        inner_ans -= int(w[i])
    # 이 부분이 결과의 전체 합계
    ans += inner_ans
print(ans)
print(eval(input()))