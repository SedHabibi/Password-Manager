from password_creator import password
from databaseManager import app_mail, connectionDB, infoStorage, name_retriever, mail_retriever, pwdTable

#Auto-generator for the passowrd.
def create(lenght):
    try:
        a = password(lenght)
        name = input("\nEnter your name : ")
        web = input("\nEnter the name of the website : ")
        mail = input('\nEnter the mail ID associated with it : ')
        infoStorage(name, web, a, mail)
        print('\nSuccessfully recorded the data.')
    except Exception as e:
        print(e)

#Manual entry by the user.
def newEntry():
    try:
        name = input("\nEnter your name : ")
        web = input("\nEnter the name of the website : ")
        pwd = input("\nEnter your password : ")
        mail = input('\nEnter the mail ID associated with it : ')
        infoStorage(name, web, pwd, mail)
        print('\nSuccesfully recorded the data.')
    except Exception as e:
        print(e)

#Secondary menu.
def main():
    #Checking if the table exists.
    try:
        connectionDB()
        pwdTable()
    except Exception as e:
        print(e)
    #Choices for the user.
    print('=' * 50)
    print("~~ MENU ~~")
    print('=' * 50)
    print("1. Generate a password.")
    print('-' * 50)
    print("2. Enter a password of your choice.")
    print('-' * 50)
    print("3. Find all the details by name.")
    print('-' * 50)
    print("4. Find all the details by email ID.")
    print('-' * 50)
    print("5. Find all apps/websites connected to an email ID.")
    print('-' * 50)
    print("6. Exit.")
    print("-" * 50)
    userInput = int(input("Choice : "))
    print('-' * 50)

    #Conditional statements for the above actions.
    if userInput == 1:
        #Computer generated password.
        try:
            connectionDB
            lenght = int(input("How long do you want your password to be : "))
            create(lenght)
        except Exception as e:
            print(e)
    elif userInput == 2:
        connectionDB
        #Custom password by the user.
        newEntry()
    elif userInput == 3:
        try:
            connectionDB()
            name = input("Please enter the name for which you want to search the records : ").strip()
            name_retriever(name)
        except Exception as e:
            print(e)
    elif userInput == 4:
        try:
            connectionDB()
            mail = input("Please enter the mail ID associated with any account : ").strip()
            mail_retriever(mail)
        except Exception as e:
            print(e)
    elif userInput == 5:
        try:
            connectionDB()
            mail = input("Please enter the mail ID associated with any account : ").strip()
            app_mail(mail)
        except Exception as e:
            print(e)
    elif userInput == 6:
        exit()
 
if __name__ == '__main__':
    main()
    while True:
        ask = input("Do you want to enter one more query [y/n]: ").lower()
        if ask == 'y':
            main()
        else:
            exit()