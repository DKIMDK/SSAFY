# DB란?
- 조직화된 데이터의 모음
 - 우리가 프로그램에서 사용할 데이터를 구조화 해서 저장해놓은 것
 - 저장, 조회 삭제, 수정 등 추가 작업은 어떻게?

- 일반적으로 DBMS(DataBase Management System)을 DB라 부름

## DB의 구성요소
- 목표: 일상 생활의 객체를 DB에 표현하고 저장
  
- 개체(Entity), 스키마(Schema), 테이블(Table)
  - 개체
    - 저장하고자 하는 실제 객체 or 개념 (ex: 고객, 학생명부..)
    - 각 개체는 필요에 따라 여러 속성으로 구성.
  - 스키마(Schema)
    - DataType
    - Entity와 속성들의 구조, 관계, 제약 조건 등을 정의한 것
    - 어떻게 구조화할 지 논리적으로 설계한 것
  - 테이블(Table)
    - 실제로 DB에 저장되는 객체
    - 구성 요소: 행렬
      - 행(Row), 레코드(Record), 튜플(Tuple)
        - 가로 줄
        - 하나의 데이터 항목
      - 열(Column), 속성(Attribute), 필드(Field)
        - 세로 줄
        - 어떤 데이터를 저장할 것인지 나타냄
- 속성(Attribute)
  - 개체의 특정 항목 (ex: 개체가 사람이라면 키, 나이, 성별 ...)
- 관계(Relationship)
  - 두 가지 이상 개체 사이의 관계
  - 두 개체를 같이 관리 하면 중복이 매우 많이 발생하는 경우 따로 관리하여 연결
  - 관계도: ERD(Entity Relationshp Diagram)
  
## DB의 종류

1. 관계형(RDBMS)
 - 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
 - 테이블 간 관계를 설정하여 여러 데이터를 조작, 관리할 수 있음
 - 장점: 무결성 (정확성, 일관성) 유지
   - 정확성: 데이터가 정확한 값을 갖는 것(제약 조건에 위반은 없는가, 누락이 없는가, 중복은 없는가..)
   - 일관성: DB 내의 모든 데이터가 일관된 상태를 유지하는 것
   - 예시) 한 테이블에서 삭제된 데이터가 다른 테이블에서 참조된다면, 자동으로 함께 삭제
 - 단점:
   - 테이블이 나뉘어져 있음
     - 쿼리문이 복잡해짐 >> 시스템 성능에 영향
     - 대용량 데이터 처리가 어렵다.
   - 데이터의 규모가 커지면 성능 개선을 해야한다.
     - 수평적 확장이 불가능
       - 수평적 확장
         - 여러 PC에서 분산하여 처리하도록 개선
         - 하나의 DBMS를 여러 서버에 분산하여 저장 및 처리
         - 분산 데이터베이스 (Distributed Database)
       - 수직적 확장
         - 더 좋은 하드웨어
2. 비관계형 (NoSQL)
 - 관계형 데이터베이스의 한계를 극복하기 위해서 사용
 - 장점:
   - 확장성: 수직, 수평적 확장 모두 가능
   - 유연성: 스키마가 고정된 RDB와 달리 스키마가 유동적이다
     - 데이터의 구조를 유연하게 변경할 수 있다.

# SQL
- SQL 명령어는 크게 세 그룹으로 분류
1. DDL (Data Definition Language)
   - 데이터베이스 구조(스키마, 테이블)를 다루기 위한 명령어
   - 실제로 유지보수 단계에서 많은 회의를 거쳐 하는 작업
     - 테이블 간 관계가 있기 때문에, 추후 변경이 굉장히 어렵다
     - 잘못 설계하면 시스템의 성능에 치명적일 수 있다.
   - 신입은 잘 안건드는 명령어, 명세서를 받고 그대로 작업하면 됨.
  
2. DML (Data Manipulation Language)
   - 데이터를 조작(CRUD)하기 위한 명령어
   - 우리가 가장 잘 알아야 할 명령어
   - 나쁜 SQL은 시스템의 성능을 나쁘게 만든다

3. DCL (Data Control Language)
  - 데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어
  - sqlite는 파일로 DB가 관리됨
    - 파일 접근 권한으로 관리가 가능하므로, 몇가지 명령어를 지원하지 않음

### SQL문을 사용하기 전 필수 지식?
- SQL: Structured Query Language (구조화된 질의 언어)의 약자
  - DB에서 데이터를 조작하고 검색하는 데 사용되는 표준 언어
- SQL문(statement)
  - 데이터를 조작하거나 검색하는 작업을 수행하는 명령어의 집합
  - ex) SELECT, INSERT, UPDATE, DELETE 
  - 여러개의 절(clause)로 구성됨
- SQL절(clause)
  - SQL문의 구성요소 중 하나
  - SQL문의 구문 구조를 완성하기 위해 사용됨
  - ex) FROM, WHERE, GROUP BY, ORDER BY, HAVING 등..
  
### 심화(나중에 공부하세요)

- 트랜잭션(Transaction)
  - 하나 이상의 SQL문을 포함하는 논리적 작업 단위
  - 여러 SQL문이 한 번에 성공해야 정상, 실패시 모두 취소를 해야 데이터의 무결성이 보장됨
  - 정상적인 성공: commit
  - 실패 >> 전체 작업을 취소(undo)하는 과정을 롤백(rollback)이라고 한다.
  - 트랜잭션의 성질(ACID)
    - 원자성(Atomicity), 일관성(Consistency), 격리성(Isolation), 영속성(Durability)