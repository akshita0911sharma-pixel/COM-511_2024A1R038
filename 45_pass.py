password=input("Enter your password: ")
if len(password)>=8 and "@" in password:
    print("valid Password")
else:
    print("Invalid Password")    
