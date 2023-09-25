'''
소 중 대 박스3
1. 같은 크기의 당근은 한 박스에
2. 상자가 비면 안됨
3. 한 상자에 N//2개 초과하는 당근 x
4. 각 상자의 개수 차이 최소

포장불가 시 -1


'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    can = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            A = carrots[:i]
            B = carrots[i:j]
            C = carrots[j:]
            if A[-1] == B[0] or B[-1] == C[0]:
                continue
            if len(A) * len(B) * len(C) == 0:
                continue
            if len(A) > N//2 or len(B) > N//2 or len(C) > N//2:
                continue
            can.append(max(abs(len(A) - len(B)), abs(len(C) - len(A)), abs(len(B) - len(C))))

    try:
        print(f'#{tc} {min(can)}')
    except:
        print(f'#{tc} -1')


