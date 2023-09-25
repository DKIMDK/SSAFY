def min_operations(start, end):
    maximum = 100000

    visited = set()  # 이미 방문한 값을 저장하기 위한 집합
    queue = [(start, 0)]  # 시작 값과 연산 횟수를 저장하는 큐

    while queue:
        value, operations = queue.pop(0)

        if value == end:
            return operations

        # 가능한 4가지 연산을 수행하여 새로운 값을 생성
        operations += 1
        possible_values = [value * 2, value // 2, value + 1, value - 1]

        for new_value in possible_values:
            if 0 <= new_value <= maximum:
                if new_value not in visited and new_value >= 1:  # 음수 값이나 이미 방문한 값은 제외
                    visited.add(new_value)
                    queue.append((new_value, operations))

    return -1  # 연산으로 도달할 수 없는 경우

# 테스트
start_value = 2
end_value = 99999
result = min_operations(start_value, end_value)
if result != -1:
    print(f"최소 연산 횟수: {result}")
else:
    print("연산으로 도달할 수 없는 경우")
