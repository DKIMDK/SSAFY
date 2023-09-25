'''
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것

입력: 문자의 총 수, 공백 후 문자열
'''
def password(lst):
    stack = []
    top = -1
    for i in lst:
        if stack and stack[top] == i:
            stack.pop()
        else:
            stack.append(i)
    ans = ''.join(stack)
    return ans

T = 1
for tc in range(1, T+1):
    str_N, str_num = input().split()
    print(password(str_num))