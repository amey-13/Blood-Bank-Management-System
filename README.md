# Blood-Bank-Management-System

###  Storyline

1.	This management system is for a blood bank with blood inventory at several location.
1.1	 Each blood inventory has a branch id, branch name, address and email id.
1.2	 A blood inventory organizes various camps for blood donation.
1.3	 A blood inventory has stock of different blood groups.

2.	The database must keep track of the blood stock available in the blood inventory.
2.1	 Each stock has a unique stock id.
2.2	 A stock has details of the blood group and the quantity.
2.3	 Each stock belongs to one specific blood inventory.

3.	The blood bank should keep the records of all the camps held.
3.1	 Each camp has a unique camp id.
3.2	 It also keeps a track of location, date and time of the camp.
3.3	 Each camp can be associated with only one blood inventory.

4.	The blood bank database keeps a track of the employees and stores their information in the database.
4.1	 The name, employee id, sex, salary, contact, qualification, designation and date of joining is stored in the database.
4.2	 Each employee has a unique id.
4.3	 Each employee belongs to one specific blood inventory.
4.4	 A blood inventory can employ various employees.
4.5	 It also keeps track of the employees who work at the camp.

5.	The blood bank needs to keep a record of its donors.
5.1	 Each donor has an ID, name, sex, contact, blood group, age and weight.
5.2	 Every donor has a unique donor ID.
5.3	 It also keeps a record of the camps in which the donor participated and the blood inventory in which the donation was done.
5.4	 A donor can participate in several camps and donate blood multiple times.

6.	The database also keeps a record of the acceptors.
6.1	 Each acceptor has an ID, name, sex, contact, blood group, age.
6.2	 Every acceptor has a unique ID.
6.3	 The name of hospital and the cause for which the blood was required is also recorded.
6.4	 An acceptor can receive blood several times.

### Components of Database Design

The entities and their respective attributes required are as follows:

1)	Donor – The blood bank has various donors who donate blood to the blood bank. Every donor has id, name, contact, age, sex, weight, blood group. A donor can donate blood multiple times.

2)	Acceptor – The blood bank has acceptors who receive blood from the blood bank. Every acceptor has id, name, contact, age, sex, weight, blood group, hospital name and cause.

3)	Blood Inventory – The blood bank has various branches that store blood known as the blood inventory. Each blood inventory has its branch ID, branch name, address and email as the key attributes.

4)	Camp – Each blood inventory organises camps through which acceptors donate blood to the blood inventory. Each camp has its unique Camp ID, location, date, time and the Branch ID of the branch which organises it which is the foreign key.

5)	Stock – Every blood inventory has its blood stock which is saved in this entity. Every stock has a Stock ID, Branch ID, Blood group and quantity.

6)	Employee – Blood bank has employees that look after the working of the blood bank. Each employee works for a specific branch and volunteers in the camps held by that particular branch.

Relationships and Cardinality:

1)	The entities Blood Inventory and Camp are connected by a relation called organized_by, since blood inventory organizes camp. Each blood inventory can organize several camps but a camp can be associated with only one blood inventory. Hence it is a one-to-many relationship. A camp cannot exist without a blood inventory. Hence there is total
participation on the many side (Camp).

2)	The entities Blood Inventory and Donor are connected by a relation called donates, since donor donates blood in the blood inventory. A donor can donate blood in several blood inventories and a blood inventory can have many donors. Hence it is a many-to-many relationship. A blood inventory cannot exist without a donor. Hence there is total participation on blood inventory side.

3)	The entities Blood Inventory and Acceptor are connected by a relation called receives, since acceptor receives blood from the blood inventory. An acceptor can receive blood from several blood inventories and a blood inventory can have many acceptors. Hence it is a many-to-many relationship. An acceptor cannot exist without blood inventory. Hence there is total participation on acceptor side.

4)	The entities Blood Inventory and Employee are connected by a relation called works_in, since employee works in the blood inventory. A blood inventory can have many employees but an employee can work for only one blood inventory. Hence it is a one-to-many relationship. A blood inventory cannot exist without an employee and an employee cannot exist without a blood inventory. Hence there is total participation on both the sides.

5)	The entities Blood Inventory and Stock are connected by a relation called has, since blood inventory keeps record of the stock of blood. A blood inventory can have stock of various blood groups but a stock can be associated with only one blood inventory. Hence it is a one-to-many relationship. A blood inventory might not have a stock of any blood group. Hence there is partial participation on blood inventory side. But a stock cannot exist without a blood inventory. Hence there is total participation on stock side.

6)	The entities Donor and Camp are connected by a relation called participated_in, since donor participates in the camp. A donor can participate in various camps and a camp can have several donors. Hence it is a many-to-many relationship. A donor cannot exist without participating in a camp. Hence there is total participation on donor side.

7)	The entities Employee and Camp are connected by a relation called works_at, since employee works at the camp. A camp can have several employees and an employees can work at many camps. Hence it is a many-to-many relationship. A camp cannot exist without an employee. Hence there is total participation on camp side.
