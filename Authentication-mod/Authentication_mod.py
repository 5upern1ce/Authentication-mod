import mysql.connector, bcrypt

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",      # or the server IP
    user="root",
    password ="saroot",
    database="logins"  # the name of the database you want to connect to
)


#Inputs the user details
def GetUserDetails():
    user = input("What is your username? \n")
    passwd = input("What is your password? \n")
    return user, passwd

#Stores User details in an SQL server
def StoreDetails(user, passwd):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO users (username, password) VALUES (%s, %s)
    """
    data = (user, passwd)

    cursor.execute(insert_query, data)
    connection.commit()
    print("User data input successfully!")



#Hashes the password
def PassHash(passwd):
    hashedpw = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()) #Hashes and creates salt
    return hashedpw

def main():
    user, passwd = GetUserDetails()
    encodedPasswd = PassHash(passwd)
    StoreDetails(user, encodedPasswd)


if __name__ == "__main__":
    if connection.is_connected:
        print("Connected successfully!")
        main()
        connection.close()
    else:
        print("Connection was unsuccessful")