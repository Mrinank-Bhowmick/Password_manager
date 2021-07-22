import hashlib
import os
import time
def eee(pw):
    p=open('rockyou.txt','r',encoding='cp850')
    e=p.readlines()
    for i in e:
        k=0
        L=len(i)
        if i[0:L-1] == pw:
            k=1
            break  
    if k==1:    
        print('\rdont use this password                       ')
        return 404
    else: 
        print('\rthis is safe to use.                         ')

def new():
    pw=input("enter your password / or enter 'g' to generate a automatic password: ")
    if pw=='g':
        def pwd_gen():
            import random
            while True:
                n=int(input('enter how long u want ur password: '))
                if n<8:
                    print('choose your length greater than 8')
                else:
                    break
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
            rand_digit = list(random.choice(DIGITS))
            rand_upper = list(random.choice(UPCASE_CHARACTERS))
            rand_lower = list(random.choice(LOCASE_CHARACTERS))
            rand_symbol = list(random.choice(SYMBOLS))
            str = rand_digit + rand_upper + rand_lower + rand_symbol
            for i in range(n-4):   
                rand_digit = list(random.choice(DIGITS))
                rand_upper = list(random.choice(UPCASE_CHARACTERS))
                rand_lower = list(random.choice(LOCASE_CHARACTERS))
                rand_symbol = list(random.choice(SYMBOLS))
                LIST=[rand_digit,rand_lower,rand_upper,rand_symbol]
                op=random.randint(0,3)
                str = LIST[op] + str
            random.shuffle(str)
            s="".join(str)
            print(s)
            usr_choice=input('would u like to keep this password? type "no" re-enter or press any key: ')
            
            if usr_choice.lower()=='no':
                s=pwd_gen()
                return s
            if usr_choice.lower() != 'no':
                return s
        pw=pwd_gen()
        return pw
    check=input('want to check is your password have been found in a data breach or not? \nif yes type "y" or else "n" :')
    if check=="y":
        print('\rplease wait we are analysing...',end="")
        eee(pw)
        c=input('would you like to keep this password? :')
        if c=="n":
            new()
    return pw

while True:
    usr_check=input('Enter your Account name : ')
    if os.path.exists(usr_check):
        break
    else:
        print('This Account does not exists.')

ls = {}
ls['name'] = input("Enter your Username: ")
ls['url'] = input("Enter url: ")
p=new()

import pickle
file = open(f"{usr_check}","rb")
emp = pickle.load(file)
from cryptography.fernet import Fernet

fer=Fernet(emp['key'])
encMessage = fer.encrypt(p.encode())
ls['password'] = encMessage
file.close()

file = open(f"{usr_check}","ab")

pickle.dump(ls, file)
file.close()
print('Done appending')
print('..........................................................................................')
