# JS 6일차
30일 온라인 강의 axios 실습
## 실생활 예시
- 할로윈 파티
  - 치킨, 피자, 족발을 배달앱을 통해 주문하자

- 제약 조건
  - 주문, 요리, 배달 3단계로 이루어져있다고 가정.
  - 각 단계에서 걸리는 시간은 랜덤
    - `Math.random() * 2000` 활용
  - 주문 함수
    - 무작위 주문 번호를 생성한다.
  - 요리 함수
    - 20% 확률로 요리가 실패한다.
  - 배달 함수
    - 10% 확률로 배달에 실패한다.

### MM 온오프라인코칭을 통해 1.배달앱.js 받기 및 nodejs 설치

- 참고
  - https://married-spot-253.notion.site/5fef18bbcd4b467fb8c7ed819250e1e8?v=b00f715ddfac4cbf89b445f4dd0a315a
  - https://nodejs.org/en LTS Version

- 코드의 문제점
  - return을 받을 수 없다
    - 실패 여부를 판단할 수가 없다
  - 순서가 마음대로
  - 
### 순서 보장 해결법

1. 콜백 함수
- 2.배달앱_callback.js 코드 참조 
  - return 없이 정상적인 흐름 or 비정상적인 흐름을 구성할 수 있음
  - 문제점: 콜백 지옥

2. Promise
  - 기초: 다음에 할 행동을 약속한다
  - resolve()
    - Promise 객체가 "성공"할 때 호출되어 결과 값을 전달
  - reject()
    - Promise 객체가 "실패"할 때 호출되어 결과 값을 전달
  - then()
    - 로직 이행 성공 시 (resolve 호출 시) then으로 넘어감
  - catch()
    - 로직 이행 실패 시 (reject 호출 시) catch로 넘어감

3. Async & Await
   - ES8(ECMA)