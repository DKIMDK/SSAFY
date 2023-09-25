import requests
from pprint import pprint
from examples.spotify_config import getHeaders
from problem_a import get_musics



def get_popular_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    musics = get_musics()
    popular_tracks = []
    for music in musics:
        if music.get('popularity') >= 90:
            popular_tracks.append(music.get('name'))
    
    return popular_tracks
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
