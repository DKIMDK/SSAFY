def binarySearch(pages, p):
    start = 1
    end = pages
    c = 0
    cnt = 1
    while p != c:
        c = int((start + end) / 2)
        if c > p:
            end = c
        else:
            start = c
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    pages, Pa, Pb  = map(int, input().split())
    A = binarySearch(pages, Pa)
    B = binarySearch(pages, Pb)
    if A == B:
        result = 0 
    elif A > B:
        result = 'B'
    else:
        result = 'A'
    print(f'#{tc} {result}')