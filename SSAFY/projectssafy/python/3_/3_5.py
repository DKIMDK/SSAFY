from book import decrease_book
number_of_people = 0

def increase_user():
    '''
    이용자 수가 늘 때마다 count +1 하는 함수입니다.
    '''
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    '''
    이용자의 이름, 연령, 주소를 받아 dictionary에 저장하고
    환영 인사를 출력하는 함수입니다.
    '''
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    increase_user()
    print(f'{name}님 환영합니다!')
    return user_info

# ws_3_3.py
def rental_book(info):
    '''
    이름을 key로, 연령을 value로 가지는 dictionary를 인자로 받아서
    연령의 10의 자리수를 빌려간 권 수로 하여 이용자의 이름과 대여 권수를
    출력하는 함수입니다.
    '''
    # info = {'김시습' : 32 ,  etc..}
    for name, age in info.items():
        number = age // 10
        decrease_book(number) # age: int, info[name]값
        print(f'{name}님이 {number}권의 책을 대여하였습니다.')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))
# create_user 함수에 name, age, address 각 list를 돌면서 인자 할당.
# dictionary들을 5개 만든 후 map type을 list로 변환, list 안에는 dict가 5개
info = dict(map(lambda dictionary : (str(dictionary['name']), int(dictionary['age'])),
                 many_user))
## 위에서 만든 many_user에서 name과 age만 가져와 mapping하는 함수를 람다로 표현
## name을 key로, age를 value로 하는 하나의 dictionary 생성 
# function : {'name' : 홍길동, 'age' : 20, 'address' : '서울'}
#            {'name' : 피카츄, 'age' : 255, 'address' : '뉴욕'}
# 에서 {'홍길동' : 20, '피카츄' : 255}을 가져오는 함수
# def name_age(dictionary):
#   dictionary2 = {dictionary['name'] : dictionary['age'] }
#   return dictionary2
## 
#print(info)
rental_book(info)