import requests
from pprint import pprint
from examples.spotify_config import getHeaders
from problem_d import get_artists_id

def get_track_id(name):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'track:{name}',  # 필수 파라미터
        'type': 'track',                  # 필수 파라미터
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params).json()
    track_list = []
    items = response.get('tracks').get('items')
    if items != []:
        for item in items:
            track_list.append(item.get('id'))
        result = track_list[0]
        return result
    if items == []:
        return ''



def recommendation(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    artist_id = get_artists_id(artist)
    track_id = get_track_id(track)
    params = {
        'seed_artists': artist_id, 
        'seed_genre': genre,
        'seed_tracks' : track_id,
        
    }
    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    
    
    response = requests.get(f'{URL}/recommendations', headers=headers, params= params).json()
    result = []
    recommends = response.get('tracks')
    for recommendation in recommends:
        result.append(recommendation.get('name'))

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
