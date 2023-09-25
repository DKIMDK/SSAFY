'''
중괄호{}와 대괄호[]가 섞여있는 문자열이 있습니다.
중괄호와 대괄호 안에는 숫자들이 적혀있습니다.

왼쪽부터 오른쪽으로 Parsing을 하며, 중괄호 / 대괄호 안에 있는 숫자들로 연산을 하려고 합니다.
대괄호[]가 나오면 합을 구하면 되고
중괄호{}가 나오면 곱을 구하면 됩니다.
예제: ABC123[10]B{3}AT[20][10]BB{2}Q

1. 0 + 10
2. 10 * 3
3. 30 + 20
4. 50 + 10
5. 60 * 2
'''

word = input()
result = 0
for i in range(len(word)):
    temp = ''

    index = i + 1
    if word[i] == '[':
        while word[index] != ']':

            temp += word[index]
            index += 1
        result += int(temp)

    elif word[i] == '{':
        while word[index] != '}':

            temp += word[index]
            index += 1
        result *= int(temp)
print(result)