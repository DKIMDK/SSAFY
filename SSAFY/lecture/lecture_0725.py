# # set method
# my_set = {1, 2, 3}

# ## remove(), discard()
# my_set.discard(2)
# print(my_set)

# #my_set.remove(10)
# print(my_set.discard(10))

# ## pop() 임의의 요소 제거 후 반환: 순서 x

# # my_set = {'c','a','d','e' , 'f','g', 'k', 'b'}
# # print(my_set.pop())
# # print(my_set.pop())
# # print(my_set.pop())
# # print(my_set.pop())
# # print(my_set.pop())
# # print(my_set.pop())
# # print(my_set.pop())

# ## update() iterable 요소를 set에 추가
# my_set.update([5,6,7,8])
# # print(my_set)

# # 집합 method: diff -, intersection &, issubset issuperset <=, union :
# my_set2 = {1,2,3}
# # print(my_set2 - my_set)
# # print(my_set - my_set2)

# # dictionary methods: get, keys, values, items, pop ..
# my_dict = {'name' : 'Alice'}
# print(my_dict.get('age','No Key'))
# print(my_dict)

# # setdefault(): get과 유사, 없으면 추가함
# print(my_dict.setdefault('country', 'KOREA'))
# print(my_dict)

# # update(): 추가, 갱신, 덮어씀
# my_dict.update(country = 'CHINA')
# print(my_dict)

# # practice: 혈액형 인원 수 세기 by dict[]
# # 결과 => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A','B', 'O','B', 'AB']
# new_dict = {}
# # blood_types를 순회하면서
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면, 
#     if blood_type in new_dict:
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면(처음 설정된다면)
#     else:
#         new_dict[blood_type] = 1
# print(new_dict)

# #practice 2: by .get
# # 결과 => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
# new_dict2 = {}
# # blood_types를 순회하면서
# for blood_type in blood_types: 
#     new_dict2[blood_type] = new_dict2.get(blood_type, 0) + 1
# print(new_dict2)

# #practice 2: by .setdefault
# # 결과 => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
# new_dict3 = {}
# # blood_types를 순회하면서
# for blood_type in blood_types: 
#     new_dict3.setdefault(blood_type, 0)
#     new_dict3[blood_type] +=1
# print(new_dict3)

# new_dict4 = {}
# # blood_types를 순회하면서
# for blood_type in blood_types: 
#     new_dict4[blood_type] = new_dict4.setdefault(blood_type, 0) +1
    
# print(new_dict4)

# # copy
# a = [1, 2, [1, 2]]
# b = a[:]
# b[2][0] = 999
# print(a, b)

# ## deep copy
# import copy
# a = [1, 2, [1, 2]]
# deep_a = copy.deepcopy(a)

# deep_a[2][0] = 999
# # print(a, deep_a)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7, 8, 9]

# set1 = set(list1)
# set2 = set(list2)

# #1. set1에 4 추가
# set1.add(4)
# print(set1)
# #2. set1에 [5,6,7] 추가
# set1.update([5,6,7])
# print(set1)
# #3. set1에서 7 제거 (by 2)
# set1.discard(7)
# print(set1)
# #4. set1 차집합 set2 출력
# print(set1-set2)
# print(set1.difference(set2))
# #5. set1 교집합 set2 출력
# print(set1 & set2)
# print(set1.intersection(set2))
# #6. set1 합집합 set2 출력
# print(set1|set2)
# print(set1.union(set2))

Eng_dict = {'plus' : ['더하기', '장점'], 
            'minus' : ['빼기', '적자'], 
            'multiply' : ['곱하기', '다양하게'], 
            'division' : ['나누기', '분열']
            }

#1 단어 입력시 뜻
def find_eng_d():
    key = input()
    print(Eng_dict[key])
    print(Eng_dict.get(key, 'No word'))
    print(Eng_dict.setdefault(key, 'No word'))
#2 단어들의 목록을 출력
print(Eng_dict.keys())

#3 다음 단어와 뜻을 추가: square 제곱, 사각형
Eng_dict['square'] = ['제곱', '사각형']
Eng_dict.setdefault('square', ['제곱', '사각형'])
Eng_dict.update(square = ['제곱', '사각형'])

print(Eng_dict)

print(Eng_dict.items())

#4 입력받은 단어와 뜻을 삭제
def del_eng_d():
    key = input()
    Eng_dict.pop(key)
    #del Eng_dict[key]

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A','B', 'O','B', 'AB']
# # 결과 => {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}
bld_dict = {}
# by counter
from collections import Counter as cnt

result = cnt(blood_types)
print(result)    