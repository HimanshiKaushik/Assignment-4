# year = a
a = int(input("ENTER THE NO. OF YEAR: "))

if(a%4==0 and a%100!=0):
    print("LEAP YEAR")
elif(a%400==0 and a%100==0) :
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
    
