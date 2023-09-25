def solution(group):
    start = 0
    end = len(group) - 1
    if start == end:
        return start + 1
    elif start == end - 1:
        return start + 1 if winner(group[start], group[end]) == group[start] else end + 1
    else:
        mid = (start + end) // 2
        winning_group1 = solution(group[start:mid + 1])
        winning_group2 = solution(group[mid + 1:end + 1])

    ans = start + winning_group1 if winner(group[start + winning_group1 - 1],
                                           group[mid + winning_group2]) == group[start + winning_group1 - 1]\
        else mid + 1 + winning_group2

    return ans

def winner(a, b):
    if (a - b == 1) or (a - b == -2):
        return a
    else:
        return b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    group = list(map(int, input().split()))
    ans = solution(group)
    print(f'#{tc} {ans}')