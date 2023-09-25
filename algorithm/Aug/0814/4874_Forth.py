'''
입력 예시
10 2 + 3 4 + *.
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + +.
'''
def solution(lst):
    stack = []
    error = False
    for i in range(len(lst)-1):
        if lst[i].isdigit():
            stack.append(lst[i])
        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if lst[i] == '+':
                    result = a + b
                if lst[i] == '-':
                    result = a - b
                if lst[i] == '*':
                    result = a * b
                if lst[i] == '/':
                    result = a // b

                stack.append(result)



            except:
                error = True
    if error or len(stack) != 1:
        return 'error'
    else:
        return stack.pop()




T = int(input())
for tc in range(1, T+1):
    lst = input().split()
    ans = solution(lst)
    print(f"#{tc} {ans}")

