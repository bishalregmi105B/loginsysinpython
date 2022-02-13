from authorizer import*

uname = input("Enter User Name")
password = input("Enter Your Password")
email = input("Enter Your Email")
whatwant = input('''Enter What do you want to do 
Signup
Login
''')
if whatwant.lower()=="signup":
    d= signup(uname,password,email)
    print(len(password))
    if d=="succ" and len(password)>=8:
        print("Signup Success")
    else:
        print("Signup Failed")
elif whatwant.lower()=="login":
    d= login(uname,password,email)
    if d=="succ":
        print("Login Success")
    else:
        print("Login Failed. Enter Correct Data")