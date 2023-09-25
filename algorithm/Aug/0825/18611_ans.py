T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    boxes = [[] for _ in range(3)]

    for carrot in carrots:
        added = False  # 당근이 추가되었는지를 나타내는 플래그 변수

        # 당근을 각 상자에 추가할 수 있는지 확인하고, 가능한 상자에 추가합니다.
        for box in boxes:
            if not added and sum(box) + carrot <= N // 2:
                box.append(carrot)
                added = True

        # 모든 상자에 추가가 불가능한 경우
        if not added:
            print(f'#{tc} -1')
            break

    # 각 상자의 개수 차이 계산
    min_diff = min(len(box) for box in boxes)
    max_diff = max(len(box) for box in boxes)
    result = max_diff - min_diff

    print(f'#{tc} {result}')
