'''
R 또는 L 문자 4개를 입력받습니다.
R을 입력받으면 숫자를 오른쪽으로 한 칸씩,
L을 입력받으면 숫자를 왼쪽으로 한 칸씩 이동.
'''
arr = [3, 5, 1, 9, 7]
def LR(arr, d):
    arr2 = []
    if d == 'L':
        k = arr.pop(0)
        arr.append(k)
    elif d == 'R':
        for i in range(4):
            arr.append(arr[i])
        for _ in range(4):
            arr.pop(0)
    return arr
for _ in range(4):
    d = input()
    arr = LR(arr, d)
print(arr)
