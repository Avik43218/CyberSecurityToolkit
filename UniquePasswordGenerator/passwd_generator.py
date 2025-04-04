from cryptography.fernet import Fernet
import backup_passwd
import mysql.connector as mc
import string , random
import os

def advanced_passwd_generator():

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_ = letters + numbers + symbols

    byte_size = int(input("Enter length of passwd: "))

    temp = random.sample(all_ , byte_size)
    final = "".join(temp)

    return final

raw_passwd = advanced_passwd_generator()

def check_validity():

    # Extract the database passwd from the binary file and decrypt it

    data_base = mc.connect(host='localhost', user='root', passwd='sample_pass', database='sample_db')
    # Replace 'sample_pass' and 'sample_db' with the actual 'database password' and 'database name' respectively
    cursor = data_base.cursor()

    cursor.execute("select passwd from storage")  # 'storage' is the name of the table I used
    rows = cursor.fetchall()

    master_key = os.getenv("MASTER_KEY").encode()
    main_key = os.getenv("ENCRYPTED_KEY").encode()

    # 'master_key' and 'main_key' are stored in environment variables

    key = Fernet(master_key).decrypt(main_key)

    gen = raw_passwd

    while True:

        duplicate_found = False

        for row in rows:

            encrypted_data = str(row[0])
            cipher = Fernet(key)
            p = cipher.decrypt(encrypted_data).decode()

            if p == gen:
                gen = advanced_passwd_generator()
                duplicate_found = True
                break

        if not duplicate_found:
            break

    print("Passwd Valid!")

    cursor.close()

    return gen

unique_passwd = check_validity()

def encrypt_passwd_func():

    master_key = os.getenv("MASTER_KEY").encode()
    main_key = os.getenv("ENCRYPTED_KEY").encode()

    # 'master_key' and 'main_key' are stored in environment variables

    key = Fernet(master_key).decrypt(main_key)

    cipher = Fernet(key)
    encrypt_final_passwd = cipher.encrypt(unique_passwd.encode()).decode()

    return encrypt_final_passwd

encrypted_passwd = encrypt_passwd_func()

def upload_to_database():

    data_base = mc.connect(host='localhost', user='root', passwd='sample_pass', database='sample_db')
    # Replace 'sample_pass' and 'sample_db' with the actual 'database password' and 'database name' respectively
    cursor = data_base.cursor()

    print("Your passwd is: ", unique_passwd)

    choice = input("Do you want to store it in database? [Y/N] ")

    if choice in 'yY':

        web = input("Enter website name: ")
        usr_name = input("Enter user name: ")
        passwd_final = encrypted_passwd

        # Now check the UID in the database and generate a unique number

        cursor.execute("select uid from storage")
        rows = cursor.fetchall()

        cursor.close()
        
        uid = random.randint(1000000, 10000000)

        while True:

            duplicate_found = False

            for row in rows:

                if uid == row[0]:
                    uid = random.randint(1000000, 10000000)
                    duplicate_found = True
                    break

            if not duplicate_found:
                break

        print("UID available!")
        new_uid = uid
        print("Your UID: ", new_uid)

        insert_db = data_base.cursor()

        query = "insert into storage values (%s, %s, %s, %s)"   
        values = (new_uid, web, usr_name, passwd_final)
        insert_db.execute(query, values)

        data_base.commit()

        insert_db.close()

    else:

        print("Copy this passwd and keep it safe: ", passwd_final)

    return None

upload_to_database()
backup_passwd.create_backup()
