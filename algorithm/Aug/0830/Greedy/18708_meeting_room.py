# N = int(input())
# hours = [0] * 100000001
# for _ in range(N):
#     start, end = map(int, input().split())
#     hours[start] += 1
#     hours[end] -= 1
#
# current_count = 0
# max_hours = 0
# for count in hours:
#     current_count += count
#     max_hours = max(max_hours, current_count)
#
# print(N - max_hours)

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))


meetings.sort(key=lambda x: x[1])

count = 1
end_time = meetings[0][1]

for i in range(1, N):
    if meetings[i][0] >= end_time:
        count += 1
        end_time = meetings[i][1]

print(count)
