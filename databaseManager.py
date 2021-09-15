#Importing the mysql connector.
import mysql.connector 
from mysql.connector import errorcode
from mysql.connector import connection

#Defining global variables.
global dbConnector

#Establishing connection with the database.
def connectionDB():
    global dbConnector
    try:
        dbConnector = mysql.connector.connect(user = 'root', password = '1234', host = 'localhost', database = 'PasswordManager')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\nSomething is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("\nDatabase does not exist")
        


#Creating a table in the database to store our data.
def pwdTable():
    #Defining the cursor for our database.
    cursor = dbConnector.cursor()
    
    #Exception handling for checking if the table's existence.
    try:
        #Creating a table if it does not exist.
        cursor.execute("CREATE TABLE pwdManager (Name varchar(255), Website varchar(255), Password varchar(255), Email_ID varchar(255))")
        print("\nTable created!")

    except:
        print("\nTable already exists!")
    

#Storing information.
def infoStorage(Name, Web, pwd, mailID):
    try:
        cursor = dbConnector.cursor()

        #Query for insertion of values in the Manager table.
        query = "INSERT INTO pwdmanager (Name, Website, Password, Email_ID) VALUES (%s, %s, %s, %s)"

        #Values to be provided by the user.
        values = (Name, Web, pwd, mailID)

        #Execution and comitting to the database.
        cursor.execute(query, values)
        dbConnector.commit()
    except Exception as e:
        print(e)

#Searching for data by name.
def name_retriever(Name):
    try:
        #Initiating the cursor.
        cursor = dbConnector.cursor()

        #Appropriate MySL statement.
        query = "SELECT * FROM pwdmanager WHERE Name = %s"
        cursor.execute(query, (Name,))

        #Fetching the records if available.
        records = cursor.fetchall()
        dbConnector.commit()

        #Printing the result.
        if len(records) > 0:
            print("\nData for the requested query : ")
            for i in records:
                print(i)

        elif len(records) == 0:
            print("\nNo data available for this query.")

    except Exception as e:
        print(e)

#Fetching data by email ID.
def mail_retriever(emailID):

    try:
        #Initiating the cursor.
        cursor = dbConnector.cursor()

        #Query to search by email ID.
        query = "SELECT * FROM pwdmanager WHERE Email_ID = %s"
        cursor.execute(query, (emailID,))

        #Fetching the records if available.
        records = cursor.fetchall()
        dbConnector.commit()

        #Printing the result.
        if len(records) > 0:
            print("\nData for the requested query : ")
            for i in records:
                print(i)

        elif len(records) == 0:
            print("\nNo data available for this query.")
    
    except Exception as e:
        print(e)

#To fetch websites/apps connected to a mail ID.
def app_mail(mail):
    try:
        cursor = dbConnector.cursor()

        #Query.
        query = "select Website from pwdmanager where Email_ID = %s"
        cursor.execute(query, (mail,))
        records = cursor.fetchall()
        dbConnector.commit()
            #Printing the result.
        if len(records) > 0:
            print("\nWebsites/Apps for the requested mail ID : ")
            for i in records:
                print(i)

        elif len(records) == 0:
            print("\nNo websites/apps associated with this mail ID.")
    except Exception as e:
        print(e)
