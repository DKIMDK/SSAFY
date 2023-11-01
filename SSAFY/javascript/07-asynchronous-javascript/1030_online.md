# JS는 Single Thread. 한 번에 여러 일을 수행할 수 없다
- 반드시 동기식이어야 함. 어떻게 비동기식으로 할 수 있을까?
> 다른곳으로 보낸다!! => JavaScript Runtime

## JavaScript Runtime
- 동작할 수 있는 환경
- 비동기 처리를 할 수 있는 환경
  - Browser
  - Node

## Browser 환경에서의 비동기 처리 관련 요소
- JavaScript Engine의 **Call Stack**
  - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)
  - 기본적인 JS의 Single Thread 작업 처리
- **Web API**
  - Browser에서 제공하는 runtime 환경
  - 시간이 소요되는 작업을 처리 (setTimeout, DOM Event(이벤트리스너), AJAX 요청 등)
- **Task Queue**
  - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
- **Event Loop**
  - Task가 들어오길 기다렸다가 들어오면 처리, 없으면 잠드는 끊임없이 돌아가는 JS 내 루프
  - Call Stack과 Task Queue를 지속적으로 모니터링
  - Call Stack이 비어있는지 확인 후 비어있다면 Task Queue에서 대기중인 오래된 작업을 Call Stack으로 Push
  
- 비동기 처리 동작 방식
  1. Call Stack으로 모두 들어감 (LIFO)
  2. 오래 걸리면 Web API로 보내 별도 처리
  3. Web API에서 처리가 끝나면 Call Stack이 아닌 Task Queue(FIFO)에 들어감
  4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크
  5. Call Stack이 비었을 때 Task Queue에서 가장 먼저 들어온 작업을 Call Stack으로 보냄

```html
<script>
    console.log('1.Hi')
    // Call Stack에 1.Hi push and pop
    setTimeout(function myFunc() {
        console.log('2.Work')
    }, 3000)
    // Call Stack에 2.Work >> 바로 Web API로 이동
    // 3초뒤에 콘솔에 출력이 된다 x, 3초 뒤에 Task Queue로 들어간다
    console.log('3.Bye')
    // Call Stack에 Bye push and pop

    // Event Loop가 Cal Stak 및 Task Queue를 끊임없이 감시 중 

    // 3초가 지난 후 Call Stack은 비어 있고 Task Queue에 work가 있으니 
    // work를 Call Stack으로 push, pop
    
</script>
```
http://latentflip.com/ << 시각화 사이트
## AJAX
- Asynchronous JacaScript + XML
- 비동기 구조 + XML (*JSON) 객체를 활용하여 비동기적으로 서버와 통신하여
- 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
  
1. XMLHttpRequest 객체 (XHR 객체)
- 서버와 상호작용 시 새로고침 없이 URL에서 데이터를 가져올 수 있음
- **이벤트 핸들러는 비동기 프로그래밍의 한 형태**
  - 이벤트가 발생할 때마다 콜백함수 제공
  - XHR = HTTP 요청 객체.
    - 요청 시 응답이 올 때까지 시간이 걸림 => 비동기 API
  - 이벤트 핸들러를 XHR 객체에 연결해 요청의 진행상태 및 최종 완료에 대한 응답을 받음

2. ***Axios***
- JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
- cf) Python에서 사용되는 HTTP 클라이언트 라이브러리: requests
- https://axios-http.com/kr/docs/intro
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
- 02-cat-api.html 및 03-cat-api-ad.html 참조
  
- 정리
  1. axios는 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
     - 브라우저를 위해 XHR 생성   
  2. 같은 방식으로 DRF로 만든 서버로 요청을 보내 데이터를 받아온 후 처리할 수 있도록 함

## Callback과 Promise
1. 비동기 처리의 단점
   - 작업이 완료되는 순서에 따라 처리
    > 코드의 실행 순서가 불명확하다는 단점
    - 콜백 함수 사용
2. 비동기 콜백
    - 작업이 완료되었을 때 실행되는 함수
    - 순차적으로 동작할 수 있게 함
    - 한계
      - 순서를 받아 다른 기능 수행하려다보니 비슷한 패턴이 발생
      - 콜백지옥(Callback Hell), Pyramid of doom
      - 가독성 저해, 유지 보수가 어려워짐
3. 프로미스
   - JS에서 비동기 작업의 결과를 나타내는 객체
   - 콜백 지옥 문제를 해결하기 위해 등장
   - Promise 기반의 클라이언트: Axios 라이브러리
     - 성공에 대한 약속 then(callback)
       - 요청이 성공하면 callback 실행
       - callback은 이전 작업의 성공 결과를 인자로 전달받음
     - 실패에 대한 약속 catch(callback)
       - then이 하나라도 실패하면 callback 실행
   - 단계가 깊어지지 않고 동일한 레벨에 chaining
4. then 메서드 chaining의 장점
    - 가독성
    - 에러 처리: 분할 처리 가능  
    - 유연성: 복잡한 비동기 흐름 구성에 유리
    - 코드관리
