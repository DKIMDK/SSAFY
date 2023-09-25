
import requests
from pprint import pprint as print

dummy_data = []
for i in range(1,10+1):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()
    user_info = {'company' : parsed_data.get('company').get('name'), 
                 'lat' : parsed_data.get('address').get('geo').get('lat')
                 if float(parsed_data.get('address').get('geo').get('lat')) < 80 else None,
                 'lng' : parsed_data.get('address').get('geo').get('lng')
                 if float(parsed_data.get('address').get('geo').get('lng')) > -80 else None,
                 'name' : parsed_data.get('name')
                   }
    dummy_data.append(user_info)

def censorship(user_dict):
    black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
    for company, name in user_dict.items():
        if company not in black_list:
            print('이상 없습니다.')
            
        else:
            print(f'{company} 소속의 {name[0]} 은/는 등록할 수 없습니다.')
            return False
    return True

def create_user(lst):
    censored_user_list = {}
    for dictionary in lst:
        if censorship({str(dictionary.get('company')): [str(dictionary.get('name'))]}):
            censored_user_list[str(dictionary.get('company'))] = [str(dictionary.get('name'))]
    return censored_user_list

censored_user_list = create_user(dummy_data)
print(censored_user_list)

# print(dummy_data)

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])
