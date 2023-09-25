def pipe(string):
    cnt = 1
    ans = 0
    for i in range(1, len(string)):
        if string[i] == '(':
            cnt += 1
        elif string[i] == ')' and string[i-1] == '(':
            cnt -= 1
            ans += cnt
        elif string[i] == ')':
            ans += 1
            cnt -= 1
    return ans

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(pipe(string))