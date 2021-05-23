def delete(mydb):

    mycursor=mydb.cursor()
    i=0
    query= " DELETE FROM Students WHERE rollno = '%d' "
    n=int(input("Enter the number of students you want to delete: "))
    while(i<=n):
        if i<1:
            rollno=int(input("Enter the roll number to remove: "))
            val=(rollno)
            mycursor.execute(query,val)
            mydb.commit()
            i=i+1
            print(rollno + " is removed from the Table")
        else:
            rollno = int(input("Enter the roll number to remove: "))
            val = (rollno)
            mycursor.execute(query, val)
            mydb.commit()
            i = i + 1
            print(rollno + " is removed from the Table")


