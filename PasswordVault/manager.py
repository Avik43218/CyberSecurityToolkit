import mysql.connector as mc
from cryptography.fernet import Fernet
import backup_passwd
import random
import os

def usr_inp():

    website = input("Enter website name: ")
    user_name = input("Enter user name: ")
    passwd = input("Enter passwd: ")

    return [website, user_name, passwd]

cred = []

def encrypt():

    while True:

        cred.append(usr_inp())

        c = input("Add another profile? [Y/N] ")

        if c == 'N':
            break
        else:
            pass

    master_key = os.getenv("MASTER_KEY").encode()
    if master_key is None:
        raise ValueError("Master Key could not be found!")
    
    encrypt_key = os.getenv("ENCRYPTED_KEY").encode()
    if encrypt_key is None:
        raise ValueError("Main Encrypted Key could not be found!")
    
    # 'master_key' and 'main_key' are stored in environment variables
    
    key = Fernet(master_key).decrypt(encrypt_key)

    encrypt_pwd = []
    for p in cred:
        
        cipher = Fernet(key)
        e = cipher.encrypt(p[2].encode())
        encrypt_pwd.append(e)

    return encrypt_pwd

data_base = mc.connect(host='localhost', user='root', passwd='sample_pass', database='sample_db')
# Replace 'sample_pass' and 'sample_db' with the actual 'database password' and 'database name' respectively
cursor = data_base.cursor()

content = encrypt()

for i in range(len(cred)):

    uid = random.randint(1000000, 10000000)
    
    query = "insert into storage values (%s, %s, %s, %s)"  # 'storage' is the name of the table I used
    values = (uid, cred[i][0], cred[i][1], content[i])
    cursor.execute(query, values)

data_base.commit()
cursor.close()

backup_passwd.create_backup()
