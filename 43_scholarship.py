cgpa=float(input("Enter your cgpa: "))
attendance=int(input("Enter your attendance:"))
national=bool(input("Do you have won any national level competition: "))
if cgpa >=8.5 and attendance>=85:
    print("Eligible")
elif national=="yes":
    print("Eligible")
else:
    print("Not eligible")     
