N = int(input())
arr = [input() for _ in range(N)]

# 입력을 원하는 형식으로 변환
arr2 = []
for i in range(len(arr[0])):
    arr2.append([arr[j][i] for j in range(len(arr))])

# 결과 출력
print(arr2)
