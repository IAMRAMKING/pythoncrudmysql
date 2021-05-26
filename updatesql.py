def update(mydb):
    mycursor = mydb.cursor()
    query= "UPDATE Students SET email= %s, depart= %s WHERE rollno= %s"
    n=input("Enter the roll number you want to update: ")
    o= input("Enter the updated email: ")
    p= input("Enter the updated department")
    val=(o,p,n)
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
