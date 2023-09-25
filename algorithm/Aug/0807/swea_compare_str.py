def compare(str1, str2):
    return str1 in str2
def BruteForce(str1, str2):
    index1 = 0  # str1의 인덱스
    index2 = 0  # str2의 인덱스
    while index1 < len(str1) and index2 < len(str2):
        if str2[index2] != str1[index1]:
            index2 = index2 - index1
            index1 = -1
        index2 = index2 + 1
        index1 = index1 + 1
    if index1 == len(str1):
        return 1 #i - M # 검색 성공
    else:
        return 0 #-1 #검색 실패
def solution(str1, str2):
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        for j in range(len(str1)):
            if str1[j] == str2[i + j]:
                cnt += 1
        if cnt == len(str1):
            result = 1
    return result
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = solution(str1, str2)

    print(f'#{tc} {result}')