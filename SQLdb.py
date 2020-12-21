import mysql.connector as mysql

try:
    mydb = mysql.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )
except:
    print("Connection Failed")

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE loginInfo (name VARCHAR(250), birthdate VARCHAR(11), email VARCHAR(40), username VARCHAR(20), password VARCHAR(250))")
#RUN THIS IF YOU ARE RUNNING IT FOR THE FIRST TIME!!!!! AFTER RUNNING IT ONCE, COMMENT IT OUT!!!!!
mycursor.execute("SELECT * FROM loginInfo")
my_result = mycursor.fetchall()
isEmpty = bool(my_result)
if isEmpty == True:
    for i in my_result:
        print(i)
elif isEmpty == False:
    print("Result is Empty!\n---------------------------------------------")

#mycursor.execute("DELETE FROM loginInfo WHERE email = ''")
#mydb.commit()

def register():
    name250 = False
    name = input("Enter your name: ")
    if len(name) > 250:
        while name250 == False:
            name = input("Name Invalid!\nEnter your name: ")
            if len(name) <= 250 and len(name) > 0:
                name250 = True
    elif len(name) == 0:
        while name250 == False:
            name = input("Name Invalid!\nEnter your name: ")
            if len(name) > 0 and len(name) <= 250:
                name250 = True
    bday11 = False
    bday = input("Enter your birthdate (mm/dd/yyyy): ")
    if len(bday) > 10:
        while bday11 == False:
            bday = input("Birthdate Invalid!\nEnter your birthdate (mm/dd/yy): ")
            if len(bday) <= 10 and len(bday) > 0:
                bday11 = True
    elif len(bday) == 0:
        while bday11 == False:
            bday = input("Birthdate Invalid!\nEnter your birthdate (mm/dd/yy): ")
            if len(bday) > 0 and len(bday) <= 10:
                bday11 = True
    email40 = False
    emailUsed = False
    email = input("Enter your email: ")
    mycursor.execute("SELECT email FROM loginInfo")
    result = mycursor.fetchall()
    is_not_empty = bool(result)
    if is_not_empty == True:
        for x in result:        
            if email in x:
                while emailUsed == False:
                    print("Email already registered!")
                    email = input("Enter your email: ")
                    if email not in x:
                        emailUsed = True
                        if len(email) > 40:
                            while email40 == False:
                                email = input("Email Invalid!\nEnter your email: ")
                                if len(email) <= 40 and len(email) > 0 and email not in x:
                                    email40 = True
                        elif len(email) == 0:
                            while email40 == False:
                                email = input("Email Invalid!\nEnter your email: ")
                                if len(email) > 0 and len(email) <= 40 and email not in x:
                                    email40 = True
        if len(email) > 40:
            while email40 == False:
                email = input("Email Invalid!\nEnter your email: ")
                if len(email) <= 40 and len(email) > 0:
                    email40 = True
        elif len(email) == 0:
            while email40 == False:
                email = input("Email Invalid!\nEnter your email: ")
                if len(email) > 0 and len(email) <= 40:
                    email40 = True                                                      
    elif len(email) > 40:
        while email40 == False:
            email = input("Email Invalid!\nEnter your email: ")
            if len(email) <= 40 and len(email) > 0:
                email40 = True
    elif len(email) == 0:
        while email40 == False:
            email = input("Email Invalid!\nEnter your email: ")
            if len(email) > 0 and len(email) <= 40:
                email40 = True
    user20 = False
    userUsed = False
    username = input("Enter your username: ")
    mycursor.execute("SELECT username FROM loginInfo")
    result = mycursor.fetchall()
    is_not_empty = bool(result)
    if is_not_empty == True:
        for x in result:        
            if username in x:
                while userUsed == False:
                    print("Username already registered!")
                    username = input("Enter your username: ")
                    if username not in x:
                        userUsed = True
                        if len(username) > 40:
                            while user20 == False:
                                username = input("Username Invalid!\nEnter your username: ")
                                if len(username) <= 40 and len(username) > 0 and username not in x:
                                    user20 = True
                        elif len(username) == 0:
                            while user20 == False:
                                username = input("Username Invalid!\nEnter your username: ")
                                if len(username) > 0 and len(username) <= 40 and username not in x:
                                    user20 = True
        if len(username) > 20:
            while user20 == False:
                username = input("Username Invalid!\nEnter your username: ")
                if len(username) <= 20 and len(username) > 0:
                    user20 = True
        elif len(username) == 0:
            while user20 == False:
                username = input("Username Invalid!\nEnter your username: ")
                if len(username) > 0 and len(username) <= 20:
                    user20 = True                                
    if len(username) > 20:
        while user20 == False:
            username = input("Username Invalid!\nEnter your username: ")
            if len(username) <= 20 and len(username) > 0:
                user20 = True
    elif len(username) == 0:
        while user20 == False:
            username = input("Username Invalid!\nEnter your username: ")
            if len(username) > 0 and len(username) <= 20:
                user20 = True
    pass8 = False
    password = input("Enter your password: ")
    if len(password) < 8:
        while pass8 == False:
            password = input("Password Too Short!\nEnter your password: ")
            if len(password) >= 8:
                pass8 = True
    mycursor.execute("SELECT email, username FROM loginInfo")
    result = mycursor.fetchall()
    is_not_empty = bool(result)
    if is_not_empty == True:
        for x in result:
            if username and email in x:
                print("email and username in use")            
            elif email in x:
                print("email already registered!")
            elif username in x:
                print("username already in use")
            else:
                nbeup = "INSERT INTO loginInfo (name, birthdate, email, username, password) VALUES (%s, %s, %s, %s, %s)"
                values = (name, bday, email, username, password)
                mycursor.execute(nbeup, values)
                mydb.commit()
                print("Registration Complete!")
    elif is_not_empty == False:
        nbeup = "INSERT INTO loginInfo (name, birthdate, email, username, password) VALUES (%s, %s, %s, %s, %s)"
        values = (name, bday, email, username, password)
        mycursor.execute(nbeup, values)
        mydb.commit()
        print("Registration Complete!")
#    mycursor.execute("SELECT * FROM loginInfo")
#    myresult = mycursor.fetchall()
#    for x in myresult:
#        print(x)

def login():
    usercheck = input("Enter your username: ")
    mycursor.execute("SELECT username FROM loginInfo")
    result = mycursor.fetchall()
    userFound = False
    for x in result:
        if usercheck in x:
            print("Username Found")
        elif usercheck not in x:
            while userFound == False:
                print("Username not Found")
                usercheck = input("Enter your username: ")
                if usercheck in x:
                    print("Username Found")
                    userFound = True
    passcheck = input("Enter your password: ")
    mycursor.execute("SELECT password FROM loginInfo")
    passResult = mycursor.fetchall()
    passFound = False
    for x in passResult:
        if passcheck in x:
            print("Password Found")
        elif passcheck not in x:
            while passFound == False:
                print("Password not Found")
                passcheck = input("Enter your password: ")
                if passcheck in x:
                    print("Password Found")
                    passFound = True

    print("Logged In!")

correctChoice = False
choice = input("Would you like to Register or Login (R|L): ")
if choice.lower() == "r":
    register()
elif choice.lower() == "l":
    login()
else:
    while correctChoice == False:
        print("Incorrect Choice")
        choice = input("Would you like to Register or Login (R|L): ")
        if choice.lower() == "r":
            register()
            correctChoice = True
        elif choice.lower() == "l":
            login()
            correctChoice = True
