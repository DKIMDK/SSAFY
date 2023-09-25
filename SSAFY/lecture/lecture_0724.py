# print(help(list))

# numbers = [1, 2, 3]
# list1 = numbers
# list2 = numbers[:]

# numbers[0] = 100

# print(list1)
# print(list2)
# a = 'Hello World'
# print(a.find('e'))

# a = "Practice makes perfect"

# #1. 문자열 a에서 'e'의 개수 세기
# print(a.count('e'))

# #2. 문자열 a에서 'i'의 위치 찾기(2가지 방법)
# print(a.find('i'))
# print(a.index('i'))
# #3. 문자열 a의 문자 사이에 . 삽입
# print('.'.join(a))
# #4. 문자열 a를 공백 기준으로 분리하여 출력
# print(a.split())
# #5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
# print(a.replace('makes', 'made'))
# #6. 문자열 a를 대문자와 소문자로 변환하여 추력
# print(a.swapcase())
# #7. 문자열 a에서 양쪽 공백 삭제하기
# print(a.strip(''))

a = ['b', 'a', 'n', 'a', 'n']
# 1. list 마지막에 a 추가
print(a.append('a'))

# 2. 오름차순 정렬
print(a.sort())
# 2-1. 내림차순
print(a.sort(reverse = True))
# 3. 뒤집기
print(a.reverse())
 #4. 리스트 a 에서 a 삭제, 출력
print(a.remove('a'))

#5. 
print(a.pop())
#6
print(a.count('n'))