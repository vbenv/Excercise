USE madang;

show tables;

CREATE TABLE Stock(
bookid INTEGER NOT NULL,
bookname VARCHAR(20) NOT NULL,
publisher VARCHAR(20),
remainder INTEGER NOT NULL CHECK(remainder >= 0),
PRIMARY KEY(bookid),
FOREIGN KEY(bookid) REFERENCES Customer(custid) ON DELETE CASCADE);

show tables;

CREATE TABLE Stock AS SELECT * FROM Book;

select * from book;

Alter TABLE Stock DROP price;

ALTER TABLE Stock ADD remainder INT CHECK (remainder >=0);

select * from Stock;

DROP TABLE Stock;

SELECT ROUND(4.875, 1); # 소수점 첫째 자리까지 반올림

SELECT custid AS '고객번호', ROUND(SUM(saleprice)/COUNT(*), -2) AS '평균금액'
FROM Orders
GROUP BY custid;

SELECT bookid, REPLACE(bookname, '야구', '농구') bookname, publisher, price
FROM Book;

SELECT bookname '제목' , char_length(bookname) '문자 수', LENGTH(bookname) 'Byte'
FROM Book;

SELECT substr(name, 1,1) '성', COUNT(*) '인원'
FROM Customer
GROUP BY substr(name, 1,1);

SELECT orderid '주문번호', orderdate '주문일', ADDDATE(orderdate, INTERVAL 10 DAY) '확정'
FROM Orders;

# NULL
SELECT name, IFNULL(phone, '연락처없음') 'phone'
FROM customer;

SELECT * FROM Orders;

SELECT orderid, orderdate, adddate(orderdate, INTERVAL 10 DAY)
FROM Orders;

select SYSDATE(), DATE_FORMAT(SYSDATE(), '%Y%m%d:%H%i%s');

select orderid, DATE_FORMAT(orderdate, '%Y-%m%-d') '주문 일',  custid, bookid
from orders
where orderdate = STR_TO_DATE('20240707', '%Y-%m-%d');

select orderid, saleprice
from orders
where saleprice <= (select AVG(saleprice) 
					from orders);
                    
select orderid, custid, saleprice
from orders
where saleprice > (select AVG(saleprice)
					from orders);
                    
select orderid, custid, saleprice
from orders od1
where saleprice > (select AVG(saleprice)
					from orders od2
					where od1.custid = od2.custid);
                    
select * from orders;                   
 
# 대한민국에 거주하는 고객에게 판매한 도서의 총판매액
SELECT SUM(saleprice) '총판매액'
FROM Orders
WHERE custid IN(SELECT custid
				FROM Customer
                WHERE address LIKE '%대한민국%');
                
SELECT orderid, saleprice
FROM Orders
WHERE saleprice > ALL(SELECT saleprice
						FROM Orders
						WHERE custid = '3');
                        
# 대한민국에 거주하는 고객에게 판매한 도서의 총판매액
SELECT saleprice
FROM Orders
WHERE EXISTS(SELECT *
					FROM Customer
                    WHERE address LIKE '%대한민국%' AND customer.custid = orders.custid);

# 스칼라 부속질의
SELECT (SELECT name 
		FROM Customer cs
        WHERE cs.custid = od.custid) 'name',
		SUM(saleprice) 'total'
FROM Orders od
GROUP BY od.custid;

ALTER TABLE Orders ADD bname VARCHAR(40);

UPDATE Orders
SET bname = (SELECT bookname
			FROM Book
			WHERE Book.bookid = Orders.bookid);

SELECT * FROM Orders;

SELECT cs.name, SUM(od.saleprice) 'total'
FROM (SELECT custid, name
	FROM Customer
    WHERE custid <=2) cs,
    Orders od
WHERE cs.custid = od.custid
GROUP BY cs.name;

# View
CREATE VIEW Vorders
AS SELECT orderid, O.custid, name, O.bookid, bookname, saleprice, orderdate
FROM Customer C, Orders O, Book B
WHERE C.custid=O.custid and B.bookid = O.bookid;

# 주소에 대한민국 포함하는 고객들로 구성된 뷰 만들고 조회.
CREATE VIEW vw_customer
AS SELECT *
FROM Customer
WHERE address LIKE '%대한민국%';

select * from vw_customer;

CREATE VIEW vw_Orders (orderid, custid, name, bookid, bookname, saleprice, orderdate)
AS SELECT od.orderid, od.custid, cs.name, od.bookid, bk.bookname, od.saleprice, od.orderdate
FROM Orders od, Customer cs, Book bk
WHERE cs.custid = od.custid and bk.bookid = od.bookid;

SELECT orderid, bookname, saleprice
FROM vw_Orders
WHERE name LIKE '김연아';

CREATE OR REPLACE VIEW vw_customer (custid, name, address)
AS SELECT custid, name, address
FROM Customer
WHERE address LIKE '%영국%';

select * from vw_customer;

show tables;

DROP VIEW vw_customer;

