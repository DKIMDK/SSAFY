T = int(input())
def find_card(cards):
    card_counts = {str(n) : 0 for n in range(10)}
    for card in cards:
        card_counts[card] += 1
    max_count = max(card_counts.values())
    max_number = max([int(num) for num, count in card_counts.items() if count == max_count])
    return max_number, max_count

for tc in range(1, T+1):
    N = int(input())
    card_list = list(input())
    max_number, max_count = find_card(card_list)
    print(f'#{tc} {max_number} {max_count}')

