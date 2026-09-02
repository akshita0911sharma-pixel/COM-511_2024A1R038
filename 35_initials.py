name=input("Enter your name: ")
initials = "".join([part[0].upper() for part in name.split()])
print(initials)  
