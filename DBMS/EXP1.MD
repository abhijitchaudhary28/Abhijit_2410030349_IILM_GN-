# EXPERIMENT 7
#### QUERY 1: Compute the no. of days remaining in this year.
SELECT DATEDIFF(LAST_DAY(MAKEDATE(YEAR(CURDATE()),365)),CURDATE()) AS days_remaining;

![alt text](<Screenshot 2026-04-05 234843.png>)

#### QUERY 2:Find the highest and lowest salaries and the difference between of them. 
SELECT MAX(sal) AS highest_salary,
       MIN(sal) AS lowest_salary,
       (MAX(sal) - MIN(sal)) AS difference
FROM employee;
![alt text](2.png)
#### QUERY 3:List employee whose commission is greater than 25 % of their salaries. 
SELECT enmae,sal,compp FROM employee WHERE compp > (0.25*sal);
![alt text](1.png)
#### QUERY 4:Make a query that displays salary in dollar format. 
SKECT ename,CONCAT('$',FORMAT(sal,2)) AS salary_in_dollars FROM employee;
![alt text](<Screenshot 2026-04-05 234919.png>)
#### QUERY 5:Create a matrix query to display the job, the salary for that job based on department number, and the total salary for that job for all departments, giving each column an appropriate heading.
SELECT job,
       SUM(CASE WHEN deptno = 10 THEN sal END) AS dept10_salary,
       SUM(CASE WHEN deptno = 20 THEN sal END) AS dept20_salary,
       SUM(CASE WHEN deptno = 30 THEN sal END) AS dept30_salary,
       SUM(sal) AS total_salary
FROM emp
GROUP BY job;
![alt text](image.png)
#### QUERY 6:Query that will display the total no of employees, and of that total the number who were hired in 1980,1981,1982 and 1983.Give appropriate column heading.
SELECT COUNT(*) AS total_employees,
       SUM(CASE WHEN YEAR(hiredate) = 1980 THEN 1 ELSE 0 END) AS hired_1980,
       SUM(CASE WHEN YEAR(hiredate) = 1981 THEN 1 ELSE 0 END) AS hired_1981,
       SUM(CASE WHEN YEAR(hiredate) = 1982 THEN 1 ELSE 0 END) AS hired_1982,
       SUM(CASE WHEN YEAR(hiredate) = 1983 THEN 1 ELSE 0 END) AS hired_1983
FROM employee;
![alt text](image-1.png)
#### QUERY 7:Query to get the last Sunday of Any Month.
SELECT DATE_SUB(LAST_DAY(CURDATE()),
INTERVAL(WEEKDAY(LAST_DAY(CURDATE()))+1)DAY) AS last_sunday;
![alt text](image-2.png)
#### QUERY 8:Display department numbers and total number of employees working in each department.
SELECT depino,COUNT(*) AS total_employees
FROM employee
GROUP BY deptno;
![alt text](image-3.png)
#### QUERY 9:Display the various jobs and total number of employees within each job group. 
SELECT job, COUNT(*) AS total_employees
FROM employee
GROUP BY job;
![alt text](image-4.png)
#### QUERY 10: Display the depart numbers and total salary for each department. 
SELECT deptno, SUM(sal) AS total_salary
FROM employee
GROUP BY deptno;
![alt text](image-5.png)