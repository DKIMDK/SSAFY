import heapq
max_heap = []
min_heap = []
mid = 500

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v)
    else:
        heapq.heappush(min_heap, v)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap)
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)
    print(mid)