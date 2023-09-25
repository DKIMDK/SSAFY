def repeatsum(num_list, m_sum):
    sum_list = []
    l = len(num_list)

    for i in range(l - m_sum + 1):
        answer = sum(num_list[i:i + m_sum])
        sum_list.append(answer)


    return (max(sum_list) - min(sum_list))

T = int(input())
for tc in range(1, T+1):
    l, m = map(int,input().split())
    num_list = list(map(int, input().split()))
    answer = repeatsum(num_list, m)
    print(f'#{tc} {answer}')