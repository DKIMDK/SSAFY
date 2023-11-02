# Vue

### 사전 준비 사항: VSC extension, chrome extension
- https://married-spot-253.notion.site/5fef18bbcd4b467fb8c7ed819250e1e8?v=b00f715ddfac4cbf89b445f4dd0a315a&p=026a610188c347a980224a848fa63bf0&pm=s

### Vue의 구조
  - Vue라는 객체에 이것저것 기능이 들어있음
  - JS의 객체 구조 분해 할당 기능으로 필요한 것만 가져와서 쓰는 식
    - 구조 분해 할당: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment
    - import와 비슷한 느낌
    ```JavaScript
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <script>
    const { createApp, ref } = Vue
    // Vue 객체 안의 createApp ref 객체만 가져와서 사용
    // 순서 상관 x, 이름은 정해진대로 써야함
    </script>
    ```

## 교안 따라 실습