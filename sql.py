import sqlite3
#(student roll number, name, department, subject, mark)
connect=sqlite3.connect("student.db")
cursor=connect.cursor()

table_info="""
Create table aiml_student(Roll_Number varchar(50) primary key,Name varchar(50),
Department varchar(50),AI_Mark int,TOC_Mark int,DBMS_Mark int,PA_Mark int,HCI_Mark int,Total_Mark int)"""

cursor.execute(table_info)
cursor.execute('''Insert into aiml_student values('71762134001','Abarna','AI & ML',75,78,87,65,90,0)''')
cursor.execute('''Insert into aiml_student values('71762134002','Abilash','AI & ML',81,87,76,85,82,0)''')
cursor.execute('''Insert into aiml_student values('71762134003','Abiles','AI & ML',84,88,93,83,84,0)''')
cursor.execute('''Insert into aiml_student values('71762134004','Aishwarya','AI & ML',91,90,88,87,93,0)''')
cursor.execute('''Insert into aiml_student values('71762134005','Ajay','AI & ML',51,48,45,65,66,0)''')
cursor.execute('''Insert into aiml_student values('71762134006','Amizhthan','AI & ML',67,68,71,67,74,0)''')
cursor.execute('''Insert into aiml_student values('71762134007','Amrutha','AI & ML',65,78,87,71,90,0)''')
cursor.execute('''Insert into aiml_student values('71762134008','Anand','AI & ML',75,81,80,77,91,0)''')
cursor.execute('''Insert into aiml_student values('71762134009','Athish','AI & ML',88,78,91,92,90,0)''')
cursor.execute('''Insert into aiml_student values('71762134010','Dakshina','AI & ML',84,72,87,78,80,0)''')
cursor.execute('''Update aiml_student set total_mark=ai_mark+toc_mark+pa_mark+hci_mark+dbms_mark''')
data=cursor.execute('''Select * from aiml_student''')

table_info="""
Create table ds_student(Roll_Number varchar(50) primary key,Name varchar(50),
Department varchar(50),BI_Mark int,DA_Mark int,DSA_Mark int,OS_Mark int,ML_Mark int,Total_Mark int)"""
cursor.execute(table_info)
cursor.execute('''Insert into ds_student values('71762133001','Akash','DS',81,87,76,85,82,0)''')
cursor.execute('''Insert into ds_student values('71762133002','Arun','DS',91,90,88,87,93,0)''')
cursor.execute('''Insert into ds_student values('71762133003','Bhuvan','DS',84,88,93,83,84,0)''')
cursor.execute('''Insert into ds_student values('71762133004','Charu','DS',75,78,87,65,90,0)''')
cursor.execute('''Insert into ds_student values('71762133005','Dinesh','DS',88,78,91,92,90,0)''')
cursor.execute('''Insert into ds_student values('71762133006','Eshwar','DS',81,87,76,85,82,0)''')
cursor.execute('''Insert into ds_student values('71762133007','Farhaan','DS',65,78,87,71,90,0)''')
cursor.execute('''Insert into ds_student values('71762133008','Farook','DS',75,81,80,77,91,0)''')
cursor.execute('''Insert into ds_student values('71762133009','Guna','DS',88,78,91,92,90,0)''')
cursor.execute('''Insert into ds_student values('71762133010','Hari','DS',67,68,71,67,74,0)''')
cursor.execute('''Update ds_student set total_mark=bi_mark+da_mark+dsa_mark+os_mark+ml_mark''')
data=cursor.execute('''Select * from ds_student''')
for i in data:
    print(i)
connect.commit()
connect.close()