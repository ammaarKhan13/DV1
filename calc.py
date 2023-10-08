a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
cal=int(input("***CALCULATOR***\n1]ADD \n2]SUBTRACT \n3]MULTIPLY \n4]DIVIDE \n5]EXIT\n"))
if (cal==1):
    print(a+b)
elif(cal==2):
    print(a-b)
elif(cal==3):
    print(a*b)
elif(cal==4):
    print(a/b)
elif(cal==5):
    print("")
else:
    print("Invalid!")