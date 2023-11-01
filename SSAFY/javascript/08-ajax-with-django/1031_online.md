# 1031 온라인

## Ajax와 서버
Remind: Ajax
- JavaScript 비동기 + XML 객체 => 홈페이지 일부만을 업데이트

- 현재 articles app: follow, like 누르면 => 모든 페이지를 새로 불러옴
- Ajax로 일부만 업데이트 하는 것이 목표

# 교안따라 실습

```bash
python manage.py migrate
python manage.py loaddata users.json articles.json
```

> 로그인 정보 = id: user1, pw: ssafy1234


- ppt 13,14p 참조. html 정보를 JS에서 읽으려면? => **data-\*** HTML문법
  - https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes
  - ### summary
    - form 요소에 지정한 data 속성을 통해 접근
    - data- 문법으로 저장한 정보는 dataset에 저장됨.
    - '-'를 기준으로 대문자로 바뀌며 이름이 저장
    - eg
    > (html)
        <form data-user-id = {{ person.pk }}  
        => (js) formTag.dataset.userId = person.pk
        
- 19p csrf => https://docs.djangoproject.com/en/4.2/howto/csrf/

- 팔로우 버튼 속성 가져오는 법
  >개발자 도구에서 elements, 팔로우 버튼 선택한 후  우클릭 > copy > copy JS path or copy selector
  
  > document.querySelector("#follow-form > input[type=submit]:nth-child(2)")
