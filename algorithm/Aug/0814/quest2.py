def check(form):
    stack = []
    for tk in form:
        if tk in ['(', '{']:
            stack.append(tk) # 괄호 추가
        elif tk == ')':
            if stack and stack[-1] == '(':
                stack.pop() # 짝이 맞으면 제거
            else:
                return 0
        elif tk == '}':
            if stack and stack[-1] == '{':
                stack.pop() # 짝이 맞으면 제거
            else:
                return 0
    return 0 if stack else 1

def op(form):
    stack = []
    for tk in form:
        if tk == ')':
            temp = 0
            while stack and stack[-1] != '(':
                temp += int(stack.pop()) # 덧셈 연산
            stack.pop() #'(' 제거
            stack.append(temp) # 연산 결과 추가
        elif tk == '}':
            temp = 1
            while stack and stack[-1] != '{':
                temp *= int(stack.pop())
            stack.pop() # '{' 제거
            stack.append(temp) # 연산 결과 추가
        else:
            stack.append(tk) # 숫자나 여는 괄호 추가
    return -1 if len(stack) != 1 else stack[0]

T = int(input())
for tc in range(1, T+1):
    form = input()
    ans = -1
    if check(form):
        ans = op(form)

    print(f'#{tc} {ans}')
