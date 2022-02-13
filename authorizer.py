from ast import And
import os

from numpy import sign 

f= open("sett.ash","a")
def login(username,password,email):
    get=open("sett.ash","r")

    lins= get.readlines()
    for line in lins:
        print(line)
        splted = line.split(",")
        print(splted)
        uname = splted[0]
        eml= splted[2]
        pss=splted[1]

        if username == uname and eml == email and pss == password:
            return "succ"
def signup(usname,email,password):
    if len(password)>=8:
        f.write(f'''{usname},{password},{email}''')
        f.close()
        return "succ"


#signup("bishal","xyz","xyz.gamil.com")