email=input("Enter your email: ")
index=email.find("@")
domain=email[index+1:]
print("Domain: ",domain)
