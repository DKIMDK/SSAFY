-- SQL문 작성 시 주의사항
-- 세미콜론(;) 기준으로 하나의 SQL문 판별

-- superheros.xlsx
-- id, 이름, 직업, 능력, 국적, 회사, 나이, (첫방영)
-- 필드 명, 타입, 제약조건 순으로 작성
-- NOT NULL: 이 필드는 NULL일 수 없다는 제약 조건
CREATE TABLE superheros(
    id INTEGER PRIMARY KEY,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER
);

-- 테이블 명 변경하기
ALTER TABLE superheros
RENAME TO superhero;

-- 새로운 컬럼 추가
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE;

-- 임시 컬럼 추가
-- 임시 컬럼 -> 곧 삭제 컬럼
-- 곧삭제 컬럼 삭제 연습
ALTER TABLE superhero
ADD COLUMN 임시 TEXT;

ALTER TABLE superhero
RENAME COLUMN 임시 TO 곧삭제;

ALTER TABLE superhero
DROP COLUMN 곧삭제;

-- 테이블 지우기
DROP TABLE superhero;