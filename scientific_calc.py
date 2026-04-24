
import math
print("---- scientific calculator----")
print("1. squre root")
print("2. power")
print("3. log")
print("4. sin")
print("5. cos")
print("6. tan")
print("7. factorial")


choice=int(input("enter your choice"))
if choice==1:
        num=float(input("enter number:"))
        result=math.sqrt(num)
elif choice==2:
        base=float(input("enter base:"))
        exp=float(input("enter exponent:"))
        result=math.pow(base,exp)
elif choice == 3:
        num=float(input("enter number:"))
        result=math.log(num)
elif choice==4:
        num=float(input("enter angle(in radians):"))
        result=math.sin(num)
elif  choice==5:
        num=float(input("enter angle(in radiand):"))
        result=math.cos(num)
elif choice==6:
        num=float(input("enter angle(in radians):"))
        result=math.tan(num)
elif choice==7:
        num=int(input("enter number:"))
        result=math.factorial(num)
else:
        result="invalid choice"
        print("result:",result)
