from my_package.math import my_math
from my_package.statistics import tools

import requests

# url = 'https://random-data-api.com/api/v2/users'

# response = requests.get(url).json()
# print(type(response))
# print(response.get('address').get('country'))
# print(response['address']['country'])

# 구구단

# for i in range(2, 9+1):
#     print(f'<{i}단>')
#     for j in range(1, 9+1):
#         print(f'{i} * {j} = {i*j}')

# n = 5
# for k in range(1,n+1):
#     print('*'*k)

## break를 이용하여 shall we close? y 입력해야 탈출

# while True:
#     k = input('Shall we close? (y/n) ')
#     if k == 'y' : 
#         print('the end')
#         break

# i = int(input())
# n= 10
# while True:
#     # 10**n으로 나눈 몫이 1의자리 수면 n자리 수
    
#     if (i // n ) < 10: break
#     n*10

# i = int(input())
# cnt = 0
# while i > 0:
#     cnt +=1
#     i //= 10
#     # 10**n으로 나눈 몫이 1의자리 수면 n자리 수
# print(cnt)

import math
numbers = [1, 4, 9, 16, 25]

sqrt_numbers = []
for number in numbers:
    sqrt_numbers.append(math.sqrt(number))

sqrt_numbers = [math.sqrt(number) for number in numbers if math.sqrt(number) % 2 == 0 ]

print(sqrt_numbers)