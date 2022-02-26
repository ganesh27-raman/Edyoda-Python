1. Count the number of Salesperson whose name begin with ‘a’/’A’.

select count(Sname) from SalesPeople
where Sname like 'a%' or 'A%';


2. Display all the Salesperson whose all orders worth is more than Rs. 2000.

select Sname sp from SalesPeople sp 
inner join Orders ors on ors.Snum = sp.Snum
where Amt > 2000;


3. Count the number of Salesperson belonging to Newyork.

select count(Sname) from SalesPerson
where City = 'Newyork';


4. Display the number of Salespeople belonging to London and belonging to Paris

Select Sname from SalesPeople
where City = 'London' or 'Paris';


5. Display the number of orders taken by each Salesperson and their date of orders.

Select onum, sname, cname
from orders, cust, salespeople
where orders.cnum = cust.cnum and
       orders.snum = salespeople.snum;