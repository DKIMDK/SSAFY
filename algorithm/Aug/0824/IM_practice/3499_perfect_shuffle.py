T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    mid = N // 2
    result = []
    if N % 2 == 0:
        deck1, deck2 = cards[:mid], cards[mid:]
    else:
        deck1, deck2 = cards[:mid+1], cards[mid+1:]
    while deck2 or deck1:
        if deck1:
            result.append(deck1.pop(0))
        if deck2:
            result.append(deck2.pop(0))
    print(f'#{tc}', *result)
