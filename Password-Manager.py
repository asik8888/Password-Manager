import random
import subprocess as sp

def mainMenu():
    print("1. Password Generator")
    print("2. Encrypt password")
    print("3. De-Crypt password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if (choice == 1):
        passwordgenerator()
    elif(choice == 2):
        encrypt()
    elif(choice == 3):
        decrypt()
    else:
        exit()

def passwordgenerator():
    char = 'abcdefghijklmnopqrstuvwxyz'
    upperchar = 'ABCDEFGHIJKLMNPPQRSTUVWXYZ'
    special = '~!@#$%^&*_+[];./\{}:">?<,|'

    npass = int(input("\nEnter number of passwords to generate? "))
    print("\nMinimum number of characters has to be 8 ")
    length = int(input("\nEnter the number of characters password should be? "))
    while(length < 8):
        length = int(input("\n Re-Enter number of characters password should be? "))

    for j in range(npass):
        password=''
        for i in range(1,length+1):
            if( i % 5 == 0):
                password += str(random.randrange(10))
            elif( i % 4 == 0):
                password += random.choice(special)
            elif( i % 2 == 0 ):
                password += random.choice(char)
            elif( i % 2 != 0):
                password += random.choice(upperchar)
        print(" \nNew Password" , j+1 , " :    ", password)
    input()
    sp.call('cls',shell=True)
    mainMenu()


def encrypt():
    print("\nEncrypt\n")
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPPQRSTUVWXYZ0123456789`!@#$%^&*()_+-='

    key = int(input('Enter a number between 1-65: '))
    while(key > 67 or key < 1):
        key = int(input(" Invalid key. Please enter key between range 1-65"))
        
    newmessage = ' '

    message = input('Enter a message: ')
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position + key) % 66
            newcharacter = alphabet[newposition]
            newmessage += newcharacter 
        else:
            newmessage += character

    print('\n\n The encypted message is :', newmessage)
    input()
    sp.call('cls',shell=True)
    mainMenu()
    
def decrypt():
    print("\nDecrypt\n")
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPPQRSTUVWXYZ0123456789`!@#$%^&*()_+-='

    key = int(input('enter a number between 1-65: '))
    newmessage = ' '

    message = input('enter a message to decrypt: ')

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            if(position-key <0):
                newposition = 66+(position-key)
            else:
                newposition = (position - key) 
            newcharacter = alphabet[newposition]
            newmessage += newcharacter 
        else:
            newmessage += character

    print('\n\n The decypted message is :', newmessage)
    input()
    sp.call('cls',shell=True)
    mainMenu()



mainMenu()
