# class student:
#     def __init__(self,name,age,score):
#         self.name,self.age,self.score=name,age,score
#     def __repr__(self):
#         return "hello world"
#     def infos(self):
#         m="hello china"
#         return m
#     def __str__(self):
#         return "sh(%s)"%self.infos()
# s1=student("bob",30,88)
# print(s1)
练习
1、查找所有蜀国人的信息
2、查找女英雄信息,只显示姓名、性别和国家
3、把曹操的国籍改为蜀国
4、把魏延的性别改为女,国籍改为 泰国
5、把id为2的记录的姓名改为 司马懿,性别改为 男,国家改为 魏国
6、删除所有的泰国人
7、删除所有的英雄记录

1、找出攻击值大于200的蜀国英雄的名字和攻击值
2、查找蜀国和魏国的英雄信息
3、将吴国英雄中攻击值为110的英雄的攻击值设置为100，防御值设置为60

1、查找攻击值在100-200之间的蜀国英雄信息
select * from sanguo where gongji between 100 and 200 and country="蜀国";
2、找到蜀国和吴国以外国家的女英雄信息
select * from sanguo where sex="女" and country not in("蜀国","吴国");

4.
1、将英雄按防御值从低到高排序
select * from sanguo order by fangyu asc;

2、将蜀国英雄按攻击值从高到低排序 
select * from sanguo where country="蜀国" order by desc;

3、将魏蜀两国的男英雄中名字为三个字的英雄按防御值升序排列
 mysql> select * from sanguo where country in("蜀国","魏国") and sex="男" and 
     name like "___" order by fangyu desc;
               
1、查找防御值倒数第2名到倒数第4名的蜀国英雄记录 
select * from sanguo where country="蜀国" order by fangyu asc limit 1,3;             
2、查找攻击值前3名且名字不为空值的蜀国英雄的姓名、攻击值和国家
select name,gongji,country from sanguo 
where country="蜀国" and name is not null order by gongji desc limit 0,3;
  

1、攻击力最强值是多少
select max(gongji) as 最强攻击力 from sanguo ;
  
 2、统计一下id,name两个字段分别有多少条记录
  select count(id),count(name) from sanguo;
   
3、统计蜀国英雄中攻击值大于200的英雄的数量
  select count(gongji) from sanguo where country="蜀国" and gongji>200;    
1、统计sanguo表中一共有几个国家
 select country from sanguo group by country;
  
2、计算所有国家的平均攻击力
  select country,avg(gongji) as pj from sanguo group by country;
  
3、查找所有国家中 英雄数量最多的 前2名 的国家名称及英雄数量
 select country,count(*) as yx from sanguo 
 group by country order by yx desc limit 0,2;
    
1、找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力
select country,avg(gongji) as pj from sanguo 
group by country having pj>105 order by pj desc 
limit 0,2;

1、sanguo表中一共有哪些个国家
select distinct country from sanguo;

2、计算蜀国一共有多少个英雄
 select count(distinct name) from sanguo where country="蜀国";

1、查询时显示所有英雄的攻击力*10
select name,country,gongji*10 from sanguo;

id int
sex enum("男","怒","保密") default "保密"
name char(5)



insert into t(id,name) values()

create table jio(
id int,
name char(5),
score float(3,1),
ponte bigint,
class varchar(20)
);　　　　　　
load data infile "/var/lib/mysql-files/AID1709.csv"
into table jio
fields terminated by ","
lines terminated by "\n";

Day03作业：
综述：两张表，一张顾客信息表customers，一张订单表orders
1、创建一张顾客信息表customers，字段要求如下：
    c_id 类型为整型，设置为主键，并设置为自增长属性
    c_name 字符类型，变长，宽度为20
    c_age 微小整型，取值范围为0~255(无符号)
    c_sex 枚举类型，要求只能在('M','F')中选择一个值
    c_city 字符类型，变长，宽度为20
    c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
    在表中任意插入3条记录,c_name为"Zhangsan","Lisi",
    "Wangwu", c_city尽量 写"Beijing","Shanghai" ......
create table customers(
c_id int primary key,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum("M","F"),
c_city varchar(20),
c_salary float(10,2))
2、创建一张订单表orders，字段要求如下：
    o_id 整型
    o_name 字符类型，变长，宽度为30
    o_price 浮点类型，整数最大为10位，小数部分为2位
    设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
    在表中任意插入5条记录(注意外键限制)
    o_name分别为"iphone","ipad","iwatch",
    "mate9","r11",其他信息自己定

3、返回customers表中，工资大于4000元，或者年龄小于29岁，
满足这样条件的前2条记录
    
4、把customers表中，年龄大于等于25岁，
并且地址是北京或者上海，这样的人的工资上调15%
            
5、把customers表中，城市为北京的顾客，
按照工资降序排列，并且只返回结果中的第一条记录
            
6、选择工资salary最少的顾客的信息
                
7、找到工资大于5000的顾客都买过哪些产品的记录明细
  
select　字段名　from 表1
　　　　　　　　inner join 表2 on 条件 inner join 表3　on 条件                
8、删除外键限制
 
 inner join 表2 on 条件 inner join 表3　on 条件               
9、删除customers主键限制
primary key
create table orders(
o_id int,
o_name varchar(30),
o_price float(10,2),
foreign key(o_id) references customers(c_id)
on delete cascade
on update cascade);

insert into orders values(1,"iphone",8700),
(2,"ipad",5600),
(3,"iwatch",2000),
(4,"mate9",9000),
(5,"r11",3000);














