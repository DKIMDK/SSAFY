def apple(lst):
    N = len(lst)
    my_loc = [0, 0]
    my_direction = 1
    cnt = 0
    kk = 1
    while kk < N:
        for i in range(N):
            for j in range(N):
                if lst[i][j] == kk:
                    apple_loc = [i, j]
                    kk += 1

                    if my_direction % 4 == 0:
                        if my_loc[0] > apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 1
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 2
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] > apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction +=k
                            my_loc = apple_loc
                        else:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc

                    elif my_direction % 4 == 1:
                        if my_loc[0] > apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 1
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] > apple_loc[1]:
                            k = 2
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        else:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                    elif my_direction % 4 == 1:
                        if my_loc[0] > apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 1
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] > apple_loc[1]:
                            k = 2
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        else:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc

                    elif my_direction % 4 == 2:
                        if my_loc[0] > apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] > apple_loc[1]:
                            k = 1
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        else:
                            k = 2
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc

                    elif my_direction % 4 == 3:
                        if my_loc[0] > apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 2
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] < apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        elif my_loc[0] < apple_loc[0] and my_loc[1] > apple_loc[1]:
                            k = 3
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc
                        else:
                            k = 1
                            cnt += k
                            my_direction += k
                            my_loc = apple_loc


    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    ans = apple(arr)
    print(f'#{tc} {ans}')