6. WAP to store one student data as a tuple: name,roll no and marks. Display grade based on marks.

stu=(("Name:","Abcd"),("Roll:",3),("Marks:",(90,80,40,70)))
average=0

for i in stu:
    if i[0]=="Marks":
        marks=i[1]
        average=sum(marks)//4

if average < 50:
    print("F")
elif average < 90 and average >80:
    print("A")
elif average < 80 and average > 50:
    print("B")
elif average <= 100 and average > 90:
    print("A+")
