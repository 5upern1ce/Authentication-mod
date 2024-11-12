import sqlite3, bcrypt

"""connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=logins;'
                      'Trusted_Connection=yes;')"""


#Inputs the username 
def UserIn():
    user = input("What is your username? \n").encode()
    return user


#Stores User in an SQL server
def StoreUser(user):
    pass


#Inputs the password
def PasswordIn():
    passwd = input("What is your password? \n").encode()
    return passwd


#Stores the Password in an SQL server
def storepass(passwd):
    pass

#Hashes the password
def PassHash(passwd):
    hashedpw = bcrypt.hashpw(passwd, bcrypt.gensalt()) 
    return hashedpw

def main():
    print(PassHash(PasswordIn()))

if __name__ == "__main__":
    main()