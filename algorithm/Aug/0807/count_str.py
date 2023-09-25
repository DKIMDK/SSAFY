def strcnt(str1, str2):
    max_cnt = 0
    for index1 in range(len(str1)):
        cnt = 0
        for index2 in range(len(str2)):
            if str1[index1] == str2[index2]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    return max_cnt

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    answer = strcnt(str1, str2)
    print(f'#{tc} {answer}')