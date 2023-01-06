# marks = a
a=int(input("ENTER THE MARKS : "))

if(a<25):
    print("GRADE F")
elif(a>=25 and a<45)  :
    print("GRADE E")
elif(a>=45 and a<50):
    print("GRADE D")
elif(a>=50 and a<60):
    print("GRADE C")
elif(a>=60 and a<80):
    print("GRADE B")
else:
    print("GRADE A")
