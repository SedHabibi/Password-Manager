from databaseManager import infoStorage
import random as r

#Function to generate a password.
def password(lenght):

    #List of all characters.
    characterList = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=']
    newpwd = []
    while len(newpwd) < lenght:
        flag = r.randint(0,len(characterList) - 1)
        check = characterList[flag]
        flag2 = r.randint(0,len(check) - 1)
        newpwd.append(check[flag2])

    new_pwd = ''.join(newpwd)
    return new_pwd



