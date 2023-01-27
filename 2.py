a=int(input("Enter the year \n"))

if a%400==0:
    print(a,"is a leap year")

elif a%100 ==0:
    print(a,"is not a leap year","\n")

elif a%4==0:
    print(a,"is a leap year")

else:
    print(a,"is not a leap year")