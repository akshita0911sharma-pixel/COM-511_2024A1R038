password = "admin123"
for i in range(3):
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Login Successful")
        break
    else:
        print("Incorrect password. Try again.")
