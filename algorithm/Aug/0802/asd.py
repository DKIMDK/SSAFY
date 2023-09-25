# 버블 정렬
numbers = [63, 31, 27, 11, 25]
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble(numbers)
print(numbers)

#카운팅 정렬: 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬
def counting(arr):
    max_value = max(arr)
    count_arr = [0] * (max_value +1)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    for i, count in enumerate(count_err):
        sorted_arr.extend([i]*count)

        return sorted_arr

list1 = [1, 4, 1, 2, 7, 5, 2]
print(counting(list1))

# 순열 : 주어진 항목들로 만들 수 있는 모든 가능한 순서 (튜플)
# itertools 모듈 사용
import itertools

 arr = []

 ## 탐욕 알고리즘: 최ㅓㅈㄱ의 선택의 모음
 ## 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을주는 문제
 # 최적의 선택 : 가장 큰 단위의 동전부터 사용
 # 실습 : 동전 종류가 100, 50, 10, 거스름돈 380
 # 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까요
def change(money, coins):
    coins.sort(reverse = True)

    change = {
        coin : 0 for coin in coins
    }
    for coin in coins:
        while money >= coin:
            money -= coin
            change[coin] += 1
    return change

result = greedy(380, [100, 50 10])
print(result)