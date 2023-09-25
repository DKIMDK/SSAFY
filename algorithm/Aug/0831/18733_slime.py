def solution(arr, total):
    if len(arr) == 1:
        return total
    else:
        arr.sort()
        k1 = arr.pop(0)
        k2 = arr.pop(0)
        k = k1 + k2
        arr.append(k)
        return solution(arr, total + k)


T = int(input())
arr = list(map(int, input().split()))
result = solution(arr, 0)
print(result)