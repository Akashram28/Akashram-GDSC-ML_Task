import os
import pandas as pd
df = pd.read_excel('Passwords.xlsx')
encrypted_password = ''
decrypted_password = ''
chars = ['A' , 'B' , 'C' , 'D' ,'E' , 'F' , 'G' , 'H' , 'I' ,'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' ,'V' , 'W' , 'X' , 'Y' , 'Z' ]
spcl = ['1' , '2' , '3' , '4' , '5' , '6' , '7' ,'8' , '9' ,'0' , '/' , '.', ',' , ':' , ';' ,'[' ,']' ,'`' , '~' ,'}' ,'{','+', '_' ,'=','-','\\','|' ,'(' ,')','!','@','#','$','%','^','&','*', '"' , "'" , '<' ,'>',' ']

while True:
    master_password = str(input('Enter your Master Password : '))
    if master_password == '123456':
        print('Access Granted\n')
        break
    else:
        print('Incorrect Password')


def encrypt_chars(i):
        global encrypted_password
        if i.islower():
            if i == chars[len(chars) -3].lower():
                char_ind = 0
            elif i == chars[len(chars)-2].lower():
                char_ind = 1
            elif i == chars[len(chars)-1].lower():
                char_ind = 2
            else:
                char_ind = chars.index(i.upper()) + 3
            encrypted_password += chars[char_ind].lower()
        else:
            if i == chars[len(chars) -3]:
                char_ind = 0
            elif i == chars[len(chars)-2]:
                char_ind = 1
            elif i == chars[len(chars)-1]:
                char_ind = 2
            else:
                char_ind = chars.index(i) + 3
            encrypted_password += chars[char_ind]

def decrypt_chars(i):
        global decrypted_password
        if i.islower():
            if i == chars[0].lower():
                char_ind = len(chars) -3
            elif i == chars[1].lower():
                char_ind = len(chars)-2
            elif i == chars[2].lower():
                char_ind = len(chars)-1
            char_ind = chars.index(i.upper()) - 3
            decrypted_password += chars[char_ind].lower()
        else:
            if i == chars[0]:
                char_ind = len(chars) -3
            elif i == chars[1]:
                char_ind = len(chars)-2
            elif i == chars[2]:
                char_ind = len(chars)-1
            else:
                char_ind = chars.index(i) - 3
            decrypted_password += chars[char_ind]

def encrypt_spcl(i):
    global encrypted_password
    if i == spcl[len(spcl) -3]:
        char_ind = 0
    elif i == spcl[len(spcl)-2]:
        char_ind = 1
    elif i == spcl[len(spcl)-1]:
        char_ind = 2
    else :
        char_ind = spcl.index(i) + 3
    encrypted_password += spcl[char_ind]

def decrypt_spcl(i):
    global decrypted_password
    if i == spcl[0]:
        char_ind = len(spcl) -3
    elif i == spcl[1]:
        char_ind = len(spcl)-2
    elif i == spcl[2]:
        char_ind = len(spcl)-1
    else :
        char_ind = spcl.index(i) - 3
    decrypted_password += spcl[char_ind]

def encrypt(password):
    global chars
    global spcl
    global encrypted_password
    
    for i in password:
        if i.upper() in chars:
            encrypt_chars(i)
        elif i in spcl:
            encrypt_spcl(i)
    password_write = f'{password} : {encrypted_password}\n'
    return encrypted_password
  
def decrypt(password):
    global chars
    global spcl
    global decrypted_password
    for i in password:
        if i.upper() in chars:
            decrypt_chars(i)
        elif i in spcl:
            decrypt_spcl(i)
    return decrypted_password
    
def get_Password():
    global decrypted_password
    global df
    account = str(input('Enter your account name : '))
    index = df[df['Account']==account].index.values[0]
    password = df._get_value(index, 'Password')
    password = decrypt(password)
    decrypted_password = ''
    return password

def create_new():
    global encrypted_password
    global df
    accountName = str(input('Enter the Account Name : '))
    password = str(input('Enter the Password : '))
    password = encrypt(password)
    newData = pd.DataFrame([{'Account': accountName,'Password' :password}])
    df = df.append(newData,ignore_index=True)
    df.to_excel("Passwords.xlsx" , index=False)
    print('Password is saved')
    encrypted_password = ''
    

print('Press 1 for setting a new account.\nPress 2 for getting your passwords.')
while True:
    user = str(input('Command : '))
    if user == '1':
        create_new()
    elif user == '2':
        print(f'Your password is : {get_Password()}\n')
    elif user == 'bye':
        break

