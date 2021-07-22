import pickle
import os
while True:
    search=input('which account do you want to search? : ')
    if os.path.exists(search):
        break
    else:
        print('This Account does not exists.')

chk_pass=input('enter the master password: ')
file = open(f"{search}","rb")

from cryptography.fernet import Fernet
import hashlib
emp = pickle.load(file)
req_key=Fernet(emp['key'])

s = hashlib.sha3_224()
encoded_str = chk_pass.encode()
obj_sha3_256 = hashlib.sha3_256(encoded_str)
hash1=obj_sha3_256.hexdigest()

if emp['usr_password'] == hash1:
    print('successfull login')
    try:
        while True:
            emp = pickle.load(file)
            try:
                name=emp['name']
                pwd=req_key.decrypt(emp['password']).decode()
                url=emp['url']
                print(f'name-{name}, password: {pwd} , url: {url}')
            except KeyError:
                continue
    except EOFError:
        pass
    file.close()
else:
    print('worng password')

