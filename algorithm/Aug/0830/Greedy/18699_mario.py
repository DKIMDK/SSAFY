N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
index = 0

for i in arr:
    if index < i:
        index = i + L - 1
        cnt += 1

print(cnt)

