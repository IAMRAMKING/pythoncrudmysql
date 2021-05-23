def create(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE Students( stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), rollno INT(15), email VARCHAR(50), depart VARCHAR(50))")