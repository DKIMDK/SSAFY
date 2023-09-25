T = int(input())
def min_max(lst):
    return max(lst) - min(lst)

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(f'#{tc} {min_max(num_list)}')