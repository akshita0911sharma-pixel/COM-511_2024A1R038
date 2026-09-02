email=input("Enter your email: ")
if "@" in email and ".com":
    print("valid email")
else:
    print("Invalid email")
