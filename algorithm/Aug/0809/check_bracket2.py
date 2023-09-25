T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for i in text:
        if i == '{' or i =='(':
            stack.append(i)
        elif stack and  i =='}' and stack[-1] == '{':
            stack.pop()
        elif stack and  i ==')' and stack[-1] == '(':
            stack.pop()
        elif i ==')' or i == '}':
            stack.append(i)
    if stack:
        result = 0
    else:
        result = 1
    print(f'#{tc} {result}')
