
num1 = int(input("enter num1 :"))
num2 = int(input("enter num2 :"))
num3 = int(input("enter num3 :"))

if (num1 > num3) & (num1 > num2):
    print("num1 is max")
elif (num2 > num3) & (num2 > num1):
    print("num2 is max")
else:
    print("num3 is max")  


