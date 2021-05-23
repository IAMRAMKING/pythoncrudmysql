def select(mydb):
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM Students")
    myresult=mycursor.fetchall()

    for x in myresult:
        print(x)
