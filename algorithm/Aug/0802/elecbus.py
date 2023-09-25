# #
# # def elec(max_battery, num_station, charging_station_list):
# #     min_charging_count = 0
# #     index = 0
# #     left_battery = max_battery
# #     stations = [0]*(num_station+1)
# #
# #     for station in charging_station_list:
# #         stations[station] = station
# #
# #     for station in stations:
# #         if station == 0:
# #             left_battery -= 1
# #             if left_battery == 0:
# #                 return 0
# #
# #         else:
# #             if ??? :
# #                 left_battery -= 1
# #             #
# #             else:
# #                 left_battery = max_battery
# #                 min_charging_count += 1
# #     return min_charging_count
# #
# # T = int(input())
# #
# # for tc in range(1, T+1):
# #     max_battery, num_station, len_list = map(int, input().split())
# #     charging_station_list = list(map(int, input().split()))
# #     answer = elec(max_battery, num_station, charging_station_list)
# #     print(f'#{tc} {answer}')
# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     ch = [0] * (N + 1)
#
#     for i in arr:
#         ch[i] += 1
#     current = 0 #현재 위치
#     count = 0
#     while current < N:
#         if ch[current + K]:
#             current += K
#             count += 1
#             # 충전소 찾기 (뒤로 한 칸씩 가면서)
#         else:
#             for j in range(1, K):
#                     #충전소를 찾으면 충전, count 증가
#                 if ch[current + K - j]:
#                     current += current + K - j
#                     count += 1
#                     break
#                     # 충전소가 없으면, count = 0 , 반복종료
#             else:
#                 count = 0
#                 break
#         #최대 거리가 도착점보다 멀거나 같으면 반복 종료
#         if current + K >= N:
#             current = N
#     print(f'#{tc} {count}')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    curr, cnt = 0, 0
    # 종점 도착할 때 까지 반복
    while curr != N:
        # curr + K 한 번 충전으로 갈 수 있는 거리, N: 종점까지 거리
        if N <= curr + K:
            curr = N
            break
        #충전소 뒤에서부터 순회
        for i in range(len(arr)-1, -1, -1):
            #한 번 충전으로 갈 수 있는 거리 이내에 충전소가 있다면
            if arr[i] <= curr + K:
                cnt += 1 # 충전 횟수 증가
                curr = arr[i] # 현재 위치를 충전소 위치로 변경
                arr = arr[i+1:] # 해당 충전소 이후의 정류장만 남기기
                break
        # 충전소를 찾지 못하였다면
            if i == 0:
                cnt = 0
                curr = N # 현재 위치를 종점으로 반복문 끝
    print(f'#{tc} {cnt}')
