def update(mydb):
    mycursor = mydb.cursor()
    query= "UPDATE Students SET email='%s', depart='%s' WHERE rollno='%d'"
    n=int(input("Enter the roll number you want to update: "))
    o= input("Enter the updated email: ")
    p= input("Enter the updated department")
    val=(n,o,p)
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
