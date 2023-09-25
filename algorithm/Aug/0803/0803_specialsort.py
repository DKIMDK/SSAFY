# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = []
#
#     while len(numbers) > 0:
#         max_value = max(numbers)
#         numbers.remove(max_value)
#         result.append(max_value)
#
#         min_value = min(numbers)
#         numbers.remove(min_value)
#         result.append(min_value)
#     print(f'#{tc}', *result[:10])

#v 2
def specialSort(lst):
    for i in range(10):
        minIdx = i
        maxIdx = i
        if i % 2 == 1:
            for j in range(i+1, len(lst)):
                if lst[minIdx] > lst[j]:
                    minIdx = j
            lst[i], lst[minIdx] = lst[minIdx], lst[i]
        else:
            for j in range(i+1, len(lst)):
                if lst[maxIdx] < lst[j]:
                    maxIdx = j
            lst[i], lst[maxIdx] = lst[maxIdx], lst[i]
    return lst[:10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = specialSort(lst)
    print(f'#{tc}' , *lst)