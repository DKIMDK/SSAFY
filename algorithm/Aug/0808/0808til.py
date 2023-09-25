# Brute Force
p = 'is' #찾을 패턴
t = 'this is a book~!' #전체 텍스트
M = len(p) #찾을 패턴의 길이
N = len(t) #전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M # 검색 성공
    else: return -1 #검색 실패

## KMP 알고리즘 인덱스 출력하는 코드.
### KMP algorithm : 하나하나 찾지말고 돌아갈 위치를 저장해서 탐색 시간을 줄임 O(N+M)
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)
    lps[0] = -1
    i = 0
    j = 0 #일치한 개수
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:  # 첫글자가 불일치했거나 일치하면
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M: # 패턴을 찾을 경우
            print(i - M, end = ' ') #패턴의 인덱스 출력
            j = lps[j]

## 보이어-무어 알고리즘: 없으면 - 찾는 문자열 길이만큼 점프, 찾는 문자열 안의 문자가 있으면 - 그거에 맞춰서 점프