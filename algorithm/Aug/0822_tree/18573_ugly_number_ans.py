import heapq
N = int(input())
K = list(map(int, input().split()))
ugly = []
heap = [1]
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

while len(ugly) < max(K):
    n = heapq.heappop(heap)     #힙에서 최소값 가져오기
    if n not in ugly:
        ugly.append(n)
        heapq.heappush(heap, n * 2)
        heapq.heappush(heap, n * 3)
        heapq.heappush(heap, n * 5)
for i in K:
    print(ugly[i - 1], end=' ')
