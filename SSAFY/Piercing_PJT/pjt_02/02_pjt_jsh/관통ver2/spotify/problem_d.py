import requests
from pprint import pprint
from examples.spotify_config import getHeaders

def get_artists_id(name):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'artist:{name}',  # 필수 파라미터
        'type': 'artist',                  # 필수 파라미터
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.

    artist_id = []
  
    items = response.get('artists').get('items')
    if items != []:
        for item in items:
            artist_id.append(item.get('id')) 
        return artist_id[0]
    elif items == []:
        return ''
   

def get_related_artists(name):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    artist_id = get_artists_id(name)
    try:
        response = requests.get(f'{URL}/artists/{artist_id}/related-artists', headers = headers).json()
        artists = response.get('artists')
        result = []
        for artist in artists:
            result.append(artist.get('name'))
    except: return 
    return result
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    # """
    print(get_related_artists('NewJeans'))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists('OldShirts'))
    # None
