from cryptography.fernet import Fernet
import mysql.connector as mc
import json, pickle
import os

def create_backup():

    dataBase = mc.connect(host='localhost', user='root', passwd='sample_pass', database='sample_db')
    # Replace 'sample_pass' and 'sample_db' with the actual 'database password' and 'database name' respectively
    cursor = dataBase.cursor()

    cursor.execute("select * from storage")  # 'storage' is the name of the table I used
    rows = cursor.fetchall()

    cursor.close()

    data_list = [list(row) for row in rows]

    json_data = json.dumps(data_list, indent=4).encode()

    master_key = os.getenv("MASTER_KEY").encode()
    main_key = os.getenv("ENCRYPTED_KEY").encode()

    # 'master_key' and 'main_key' are stored in environment variables

    key = Fernet(master_key).decrypt(main_key)

    encrypted_backup_data = Fernet(key).encrypt(json_data).decode()

    with open(r"backup.dat", 'wb') as file:
        pickle.dump(encrypted_backup_data, file, protocol=pickle.HIGHEST_PROTOCOL)

    file.close()
    print("Backup created")

def load_backup():
    
    with open(r"backup.dat", 'rb') as file:
        content = pickle.load(file)

    file.close()

    master_key = os.getenv("MASTER_KEY").encode()
    main_key = os.getenv("ENCRYPTED_KEY").encode()

    key = Fernet(master_key).decrypt(main_key)

    decrypted_content = Fernet(key).decrypt(content.encode()).decode()

    return decrypted_content

