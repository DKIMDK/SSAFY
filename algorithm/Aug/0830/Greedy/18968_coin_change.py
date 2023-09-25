coins = [500, 100, 50, 10]
K = int(input())
total = 0
cnt = 0
index = 0
while total < K:
    if coins[index] <= K - total:
        cnt += 1
        total += coins[index]
    else:
        index += 1
print(cnt)