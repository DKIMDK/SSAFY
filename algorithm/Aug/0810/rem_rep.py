def solution(chars):
    stack = []
    for char in chars:
        # 만약 반복 문자라면 (stack에 문자가 있고, 현재 스택의 마지막 문자와 같다면)
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

T = int(input())
for tc in range(1, T + 1):
    chars = input()
    answer = solution(chars)
    print(f'#{tc} {answer}')