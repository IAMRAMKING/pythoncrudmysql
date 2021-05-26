def insert(mydb):
    mycursor = mydb.cursor()
    i=0
    query = "INSERT INTO Students VALUES (NULL,%s, %s, %s, %s)"
    n= input("Enter the number of students you want to enter in Student Database: ")
    while(i<int(n)):
        name=input("Enter the name: ")
        rollno= input("Enter the roll number: ")
        email=input("Enter the email: ")
        depart= input("Enter the department: ")
        val=(name,rollno,email,depart)
        mycursor.execute(query,val)
        mydb.commit()
        i=i+1
    print((i+"record inserted."))
