import pymysql
import random
import time


db = pymysql.connect(host="localhost",
user="root", password="mingle4860~!",
charset="utf8")

cursor = db.cursor()
cursor.execute('USE USERNAME;')



#showlist = []
while True:
    lorr = input("login or register: ")
    if lorr == "login":
        loginuser = input("username: ")
        loginuser2 = "'" + loginuser + "'"
        loginuser3 = '"' + loginuser + '"'
        loginpassword = input("userpassword: ")
        loginpassword2 = "'" + loginpassword + "'"
        cursor.execute('SELECT 1 FROM Information_schema.tables                                                                                       \n WHERE table_name = ' + loginuser2 + '                                                                                           \n AND table_schema = ' + "'" + "USERNAME" + "'" + '                                                                                            \n ;')
        showloginuser = cursor.fetchall()
        
        
        
        cursor.execute('SELECT * FROM ' + loginuser + ' USERPASSWORD;')
        showloginpassword = cursor.fetchall()
    
            
        
        
        
        
        
        
         
        
        if showloginuser == ((1,),):
            
            if showloginpassword[0] == (loginpassword,):
                cursor.execute('USE TEST;')
                db.commit()
                break
            else:
                print("ERROR")
        else:
            print("ERROR")

    elif lorr == "register":
        registeruser = input("username: ")
        registeruser2 = "'" + registeruser + "'"
        cursor.execute('SELECT 1 FROM Information_schema.tables                                                                                       \n WHERE table_name = ' + registeruser2 + '                                                                                           \n AND table_schema = ' + "'" + "USERNAME" + "'" + '                                                                                            \n ;')
        registerusershow = cursor.fetchall()
        if registerusershow ==  ((1,),):
            print("ERROR")
        elif "$" in registeruser:
            print("ERROR")    
        else:    
            registerpassword = input("password: ")

            registerpassword2 = "'" + registerpassword + "'"
            cursor.execute('CREATE TABLE ' + registeruser + ' (     \n                                                            USERPASSWORD VARCHAR(20000)     \n  );')
            cursor.execute('INSERT INTO ' + registeruser + ' VALUES (' + registerpassword2 + ');')
            #cursor.execute('USE TEST;')
            #cursor.execute('CREATE TABLE ' + registeruser + ' (   \n       HELLO VARCHAR(1)  \n  );')
            cursor.execute('USE USERNAME;')
            db.commit()           
        


    
    




while True:
    a = input("?%" + loginuser + "@#>>> ")
    if a == "show list":
        
        cursor.execute('show tables;')
        showlist = cursor.fetchall()
        print(showlist)
        db.commit()
        
    elif a == "add list":
        addlist = input("@#>>> ")
        addlist2 = addlist
        addlist3 = input("@#>>> ")
        addlist4 = "'" + addlist3 + "'"
        cursor.execute('CREATE TABLE ' + addlist2 + "$" + loginuser + ' ( \n                                                                                                  ' + addlist2 + ' VARCHAR(2000)                                                                                               );         ')
        
        cursor.execute('INSERT INTO ' + addlist2 + "$" + loginuser + ' VALUES' + '(' + addlist4 + ');')
        db.commit()
        
        
    elif a == "remove list":
        removelist = input("@#>>> ")
        
        
        
        removelist2 = removelist

        
        cursor.execute('DROP TABLE ' + removelist2 + "$" + loginuser + ';')
        db.commit()


    elif a == "show val":
        showval = input("@#>>> ")

        cursor.execute('SELECT * FROM ' + showval + ';')
        showval2 = cursor.fetchall()
        print(showval2)
        db.commit()


    elif a == "remove all val":
        removeval = input("@#>>> ")

        cursor.execute('TRUNCATE TABLE ' + removeval + "$" + loginuser + ';')

        db.commit()

    elif a == "add val":
        addval = input("@#>>> ")
        addval2 = input("@#>>> ")
        addval3 = "'" + addval2 + "'"

        cursor.execute('INSERT INTO ' + addval + "$" + loginuser + ' VALUES' + '(' + addval3 + ');')
        db.commit()


    elif a == "update val":
        updateval = input("@#>>> ")
        updatewhere = input("@#>>> ")
        updatewhere2 = "'" + updatewhere + "'"
        updateset = input("@#>>> ")
        updateset2 = "'" + updateset + "'"
        cursor.execute('UPDATE ' + updateval + "$" + loginuser + ' SET ' + updateval + ' = ' + updateset2 + ' WHERE ' + updateval + ' = ' + updatewhere2 + ';')
        db.commit()


    elif a == "remove val":
        removevallwhere = input("@#>>> ")
        removevall = input("@#>>> ")
        removevall2 = "'" + removevall + "'"
        cursor.execute('DELETE FROM ' + removevallwhere + "$" + loginuser + ' WHERE ' + removevallwhere + ' = ' + removevall2 + ';')
        db.commit()


    elif a == "search list":
        searchlist = input("@#>>> ")
        serchlist2 = "'%" + searchlist + "%'"
        cursor.execute('SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = SCHEMA() AND TABLE_NAME LIKE '+ serchlist2 + ';')
        showsearch = cursor.fetchall()
        print(showsearch)
        db.commit()   

            

    elif a == "exit":
        db.close()
        exit()

    elif a == "help":
        print(" show list: show text in list \n add list: add text in list \n remove list: remove text in list \n exit: exit program")
        

    else:
        print("ERROR")
    
        
    
    
    
    

#a = "'Hello'"
#b = "'asdf'"


#cursor.execute('USE TEST;')



#db.commit()
#db.close()


"""if a == "show user":
        
        cursor.execute('show tables;')
        showlist = cursor.fetchall()
        print(showlist)
        db.commit()
        
    elif a == "add list":
        addlist = input("@#>>> ")
        addlist2 = addlist
        addlist3 = input("@#>>> ")
        addlist4 = "'" + addlist3 + "'"
        cursor.execute('CREATE TABLE ' + addlist2 + ' ( \n                                                                                                  ' + addlist2 + ' VARCHAR(2000)                                                                                               );         ')
        
        cursor.execute('INSERT INTO ' + addlist2 + ' VALUES' + '(' + addlist4 + ');')
        db.commit()
        
        
    elif a == "remove list":
        removelist = input("@#>>> ")
        
        
        
        removelist2 = removelist

        
        cursor.execute('DROP TABLE ' + removelist2 + ';')
        db.commit()


    elif a == "show val":
        showval = input("@#>>> ")
        showval3 = input("@#>>> ")

        cursor.execute('SELECT ' + showval3 + ' FROM ' + showval + ';')
        showval2 = cursor.fetchall()
        print(showval2)
        db.commit()


    elif a == "remove all val":
        removeval = input("@#>>> ")

        cursor.execute('TRUNCATE TABLE ' + removeval + ';')

        db.commit()

    elif a == "add val":
        addval = input("@#>>> ")
        addval2 = input("@#>>> ")
        addval3 = "'" + addval2 + "'"

        cursor.execute('INSERT INTO ' + addval + ' VALUES' + '(' + addval3 + ');')
        db.commit()


    elif a == "update val":
        updateval = input("@#>>> ")
        updatewhere = input("@#>>> ")
        updatewhere2 = "'" + updatewhere + "'"
        updateset = input("@#>>> ")
        updateset2 = "'" + updateset + "'"
        cursor.execute('UPDATE ' + updateval + ' SET ' + updateval + ' = ' + updateset2 + ' WHERE ' + updateval + ' = ' + updatewhere2 + ';')
        db.commit()


    elif a == "remove val":
        removevallwhere = input("@#>>> ")
        removevall = input("@#>>> ")
        removevall2 = "'" + removevall + "'"
        cursor.execute('DELETE FROM ' + removevallwhere + ' WHERE ' + removevallwhere + ' = ' + removevall2 + ';')
        db.commit()


    elif a == "show list":
        cursor.execute('SELECT COLUMN_NAME                                                                                                   \n FROM    INFORMATION_SCHEMA.COLUMNS                                                                                   \n WHERE   TABLE_SCHEMA = ' + "'" + "test" + "'" + '                                                                                        \n ORDER BY TABLE_NAME, ORDINAL_POSITION;')   
        showCOLUMN = cursor.fetchall()
        print(showCOLUMN)
        db.commit()
        
            

    elif a == "exit":
        db.close()
        exit()

    elif a == "help":
        print(" show list: show text in list \n add list: add text in list \n remove list: remove text in list \n exit: exit program")
        

    else:
        print("ERROR")"""



