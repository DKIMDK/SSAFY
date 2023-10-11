-- 01. Querying data
SELECT
  LastName, FirstName
FROM
  employees;

SELECT * FROM employees;

SELECT FirstName AS '이름'
FROM employees;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM tracks;

-- 02. Sorting data
SELECT FirstName
FROM employees
ORDER BY FirstName;

SELECT 
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;

SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
order BY
  Milliseconds DESC;


-- NULL 정렬 예시
SELECT ReportsTo
FROM employees
ORDER BY ReportsTo;

-- 03. Filtering data

SELECT DISTINCT Country 
FROM customers;

SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

SELECT LastName, FirstName, Company
FROM customers
WHERE Company IS NULL
OR Country = 'USA';

SELECT Name, Bytes
FROM tracks
WHERE Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes DESC;

SELECT LastName, FirstName, Country
FROM customers
WHERE Country IN ('Canada', 'Germany', 'France')
ORDER BY Country;

SELECT LastName, FirstName, Country
FROM customers
WHERE Country NOT IN ('Canada', 'Germany', 'France')
ORDER BY Country;

SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son';

SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE '___a';

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 3, 4;

-- 04. Grouping data
SELECT Country, COUNT(*)
FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC;

SELECT Composer, Bytes, AVG(Bytes)
FROM tracks
WHERE 
GROUP BY Composer
ORDER BY AVG(Bytes) DESC;

SELECT Composer, AVG(Milliseconds / 60000) AS avgMin
FROM tracks
GROUP BY Composer
HAVING avgMin < 10;

-- 에러


-- 에러 해결
