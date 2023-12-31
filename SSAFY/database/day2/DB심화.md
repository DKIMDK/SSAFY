# DB 심화

오후 실습 내용

## DB 관계 종류

- 1:1
  - A 테이블의 하나의 레코드가 B 테이블의 하나의 레코드와 연결된 경우
  - ex) 사용자:프로필, 주문:결제 정보
- 1:N
  - A 테이블의 하나의 레코드가 B 테이블의 여러 레코드와 연결된 경우
  - ex) 게시글:댓글, 반:교육생
- M:N
  - A 테이블의 여러 레코드가 B 테이블의 여러 레코드와 연결된 경우
  - ex) 게시글:좋아요를 누른 유저, 학생:과목

## DB에서 KEY란?
- 데이터베이스 테이블에서 특정 레코드(행)를 고유하게 식별할 수 있는 필드 또는 필드 집합
  - 데이터를 검색하거나 조작할 때, KEY 값을 사용해서 특정 레코드를 식별

    ## KEY 종류
    1. 기본키(Primary Key)
       - 테이블 내에서 각각의 레코드를 식별하는 역할을 수행하는 필드
       - NULL 값을 가질 수 없는 유일한 값 (중복 x, null x)
    2. 외래키(Foreign Key)
       - 하나의 테이블에서 다른 테이블의 기본키(PK)를 참조하는 필드
       - 두 개 이상의 테이블을 연결할 때 사용
       - 반드시 써야 할까? NO, But 관리가 용이 (무결성)
       - 장점: 데이터의 무결성 보장
       - 단점: 체크해야할 사항이 많아짐 -> 리소스(오버헤드)가 더 발생
   
    [참고]
    3. 후보키
    4. 복합키
    5. 대체키
    6. 슈퍼키
## 정규화(테이블 분리하기)
- 데이터의 구조를 더 좋은 구조로 바꾸는 과정
  - 데이터를 나누거나 합치는 과정
- 목표
  - 데이터의 중복 최소화
  - 데이터의 무결성 보장
- 6단계의 정규형
  - [사전지식] 다음 정규형을 위해서는 이전 정규형이 반드시 완료되어야 한다.   
  - 기본 정규형(4개)
    - 제1정규형(1NF)
      - 모든 속성이 원자값(Atomic Value)을 가지도록 테이블을 구성하는 것
      - 즉, 모든 속성이 하나의 값을 가지는 것
      - 목표: 테이블 간 중복되는 데이터가 없도록 하기 위함
    - 제2정규형(2NF)
      - 테이블이 1NF 이어야 한다.
      - 테이블 내의 모든 컬럼은 해당 테이블의 주 식별자(PK)에만 종속되어야 한다.
      - 목표: 관계가 없는 데이터끼리 묶지 않기 위해서 따로 분리하는 과정
    - 제3정규형(3NF)
      - 
    - 보이스/코드 정규형(BCNF)
  
  - 고급 정규형(2개)
## JOIN
- CROSS JOIN
  - 두 테이블의 가능한 모든 조합을 선택
- INNER JOIN
  - 두 테이블에서 일치하는 값을 가진 행들만 선택
  - NULL X
- LEFT JOIN
  - 왼쪽 테이블 기준으로 오른쪽 테이블에서 일치하는 행을 선택 후 Join
  - NULL O