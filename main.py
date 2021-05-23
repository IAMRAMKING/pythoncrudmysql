import mysql.connector
import createsql
import insertsql
import updatesql
import selectsql
import deletesql

class Jdbc:
    def choice(self):
        inp=input("Choose the below options to perform \n 1.Create \n 2.Insert \n 3.Select \n 4.Update \n 5.Delete \n Enter the Choice here: ")
        return inp
    def jdbcconnection(self,i_input):
        mydb=mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="123ram123",
                                     database="vivek")
        if i_input=='1':
            createsql.create(mydb)
        elif i_input=='2':
            insertsql.insert(mydb)
        elif i_input=='3':
            selectsql.select(mydb)
        elif i_input=='4':
            updatesql.update(mydb)
        elif i_input=='5':
            deletesql.delete(mydb)

j1=Jdbc()
input=j1.choice()
j1.jdbcconnection(input)