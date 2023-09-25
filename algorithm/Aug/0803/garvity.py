'''
가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라

[제약 사항]
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고 그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    maxv = 0
### box 예시 [100 99 95 99 100 0 1 2 5]
    for now, box in enumerate(boxes):
        fall = 0
        for next in range(now +1, len(boxes)):
            if box > boxes[next]:
                fall += 1
        maxv = max(maxv, fall)
    print(f'#{tc} {maxv}')