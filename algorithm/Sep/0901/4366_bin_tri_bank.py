# N자리 2진수가 주어졌을 때 내가 얻을 수 있는 답안은 N개
# N개의 답을 얻는 방법ㅇ느 for i 0 > N-1: binary = a^(1<<i), lst.append(binary)
## N개를 3진수와 비교해서 값을찾기

T = int(input())
for tc in range(1, T+1):
    bin = input()
    tri = list(map(int, input()))

    N = len(bin)
    M = len(tri)
    ans = 0

    binary = int(bin, 2)
    bin_list = [0] * N
    for i in range(N):
        bin_list[i] = binary ^ (1 << i)

    for i in range(M):          # 3진수의 tri[i] 자리를 바꾼 숫자 만들기
        num1 = 0
        num2 = 0
        for j in range(M):
            if i != j:
                num1 = num1*3 + tri[j]
                num2 = num2*3 + tri[j]
            else:
                num1 = num1 * 3 + (tri[j] + 1) % 3
                num2 = num2 * 3 + (tri[j] + 2) % 3

        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f'#{tc} {ans}')