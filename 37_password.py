password=input("Enter your password: ")
if "@" in password and len(password)>=8:
    print("valid password")
else:
    print("Invalid Password")
