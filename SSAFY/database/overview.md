# 1일차

- pip
  - 파이썬 패키지 관리자
- 가상 환경
  - 여러 version을 한 환경에서 관리

- Django
  - 웹 개발 프레임워크
  - - Framework VS library
  - Django의 핵심 요소 - MTV Design Pattern (== MVC)
    - What is Design Pattern? 거인의 어깨..
    - url -> view -> model(-> db), template(html)
- 사용자 입력
  - 기존 input 태그 -> Django: Form
    - Form, ModelForm
    - Form을 더 잘 쓰는 법: widget
    - Form vs ModelForm
      - 사용자 입력을 models.py에 정의한 필드'만' 쓰는 지 여부
        - ModelForm: 정의한 필드만 입력받을 때
        - Form: 추가적인 내용을 입력받을 때

        ## 공부 시 Tip
        ### 구현이 목적 x, 이해 + 스스로 구현 -> 많이 틀려보는 것

...

- 사용자 인증 관리 구현
- login logout
### 오늘 수업을 들은 후
  - 쿠키와 세션의 개념 및 차이점 <- 중요
  - Django 인증 시스템을 활용하는 방법(오늘~내일)

### Django Auth

- HTTP의 특성
  - What is HTTP?
    - HyperText Transfer Protocol
    - 웹에서의 프로토콜(통신규약)
  - HTTP의 특징
    - 비연결 지향 (Connectionless)
      - 서버가 클라이언트의 요청을 처리한 후에 연결을 끊음
      - why? 인터넷 상에서 불특정 다수에게 정보를 제공하는 것을 기반으로 설계
        - 불특정 다수가 모두 연결을 유지하면.. 감당 x
        - 연결 유지보다는 더 많이 새로운 연결을 할 수 있게 설계
      - 단점
        - 매 요청 시 연결 및 해제 -> 리소스가 추가적으로 발생
    - 무상태 (Stateless)
      - 서버가 클라이언트의 정보(상태)를 저장하고 있지 않음
      - 요청을 보낼 때 클라이언트의 모든 정보를 같이 주어야 함
        - 장점: 서버의 부담 최소화
        - 단점: 요청이 복잡해짐
  - 공통점: 내가 누구인지 요청 시 마다 보내주어야 한다.
    - 이를 위해 쿠키와 세션 사용

  - 쿠키: "클라이언트(Browser)"에 저장하는 작은 데이터 조각 
    - 쿠키의 최대 크기, 쿠키 최대 수량은 브라우저마다 다름
      - Chrome: 4MB, 최대 180 여개
    - 요청을 보낼 때, 쿠키도 함께 전송
      - 장점: 서버의 부담 최소화
      - 단점: 보안에 비교적 취약
  
  - 세션: 서버에 데이터를 저장하고, key(세션ID)를 클라이언트에 부여
    - 요청 시 마다 key를 전달 -> 서버는 해당 key를 이용하여 사용자 데이터를 조회
    - 장점: 비교적 보안이 좋다
    - 단점: 저장된 데이터를 서버가 열어보아야 함 >> 서버에 부담

- JWT(Json Web Token)
  - 반드시 알아야 할 사용자 인증 구현 방식