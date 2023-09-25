T = int(input())
for tc in range(1, T + 1):
    text = input()
    # max_len 10
    for i in range(1, 10 + 1):
        # from 0 to i-1 == (i to 2*i -1)
        if text[:i] == text[i:i*2] and text[i:i*2] == text[i*2:i*3]:
            print(f'#{tc} {i}')
            break