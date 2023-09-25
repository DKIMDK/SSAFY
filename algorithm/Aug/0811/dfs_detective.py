'''
추적을 시작할 index를 입력받으세요.
만약 5를 입력받았다면, 5번 index부터 추적을 시작합니다.
5번 index를 살펴보면 범인은 4번 index에서 출발했고, 9시에 도착했다는 것을 알 수 있습니다.
4번 index를 살펴보면 범인은 2번 index에서 출발했고, 8시에 도착했다는 것을 알 수 있습니다.
2번 index를 살펴보면 범인은 0번 index에서 출발했고, 5시에 도착했다는 것을 알 수 있습니다.
추적해가면 마지막에는 -1에 도달합니다.
-1이 있는 곳에서 범죄자를 잡을 수 있습니다.
범인은 0번 index부터 몇 시에 몇 번 index로 이동했는지 순서대로 출력하세요
(using 재귀)

입력
추적을 시작할 index를 입력받습니다 (0<=index <=6)

5

출력
A번 index(B)의 형태로 추적상황을 출력합니다.
0번 index(출발)
2번 index(5시)
4번 index(8시)
5번 index(9시)
'''

evid = [-1, 0, 0, 1, 2, 4, 4]
time_stamp = [8, 3, 5, 6, 8, 9, 10]
def solution(index, stack = []):

    if index == 0:
        print('0번 index(출발)')
        while stack:
            k = stack.pop()
            print(f'{k}번 index({time_stamp[k]}시)')

    else:
        stack.append(index)
        solution(evid[index], stack)


def solution2(index):

    if index == 0:
        print('0번 index(출발)')
    else:
        solution(evid[index])
        print(f'{index}번 index ({time_stamp[index]}시)')

def DFS(idx, time):
    if evid[idx] == -1:
        print(f'{idx}번 index(출발)')
        return

    DFS(evid[idx], time_stamp[idx])
    print(f'{idx}번 index({time_stamp[idx]}시)')
solution2(5)
DFS(5, time_stamp[5])