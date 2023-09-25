'''
괄호검사
안쪽 괄호 먼저 연산
() 안은 더한다
{} 안은 곱한다
괄호 짝이 안맞으면 -1
'''
def solution(string):
    stack = []

    for char in string:
        if char == '(' or char =='{':
            stack.append(char)

        elif char == ')':
            temp = 0
            while stack[-1] != '(':
                try:
                    temp += stack.pop()
                except:
                    return -1
            stack.pop()
            stack.append(temp)
        elif char == '}':
            temp = 1
            while stack[-1] != '{':
                try:
                    temp *= stack.pop()
                except:
                    return -1
            stack.pop()
            stack.append(temp)
        else:
            stack.append(int(char))
    if len(stack) != 1:
        return -1
    else:
        return stack[0]

T = int(input())
for tc in range(1, T+1):
    string = input()
    ans = solution(string)
    print(f'#{tc} {ans}')