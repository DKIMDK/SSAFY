import requests
import json

# url = 'htttps://fakestoreapi.com/carts'
# data = requests.get(url).json()

## json_data
json_data = '''
{
    "name" : "김싸피",
    "age" : 28,
    "hobbies" : [
        "공부하기",
        "복습하기"
    ]
}
'''

data = json.loads(json_data)
print(data)

name = data.get('name')