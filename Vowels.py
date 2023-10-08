str=input("Enter a string: ")
vowels="aeiouAEIOU"
c=0
for i in str:
    if i in vowels:
        c+=1
print("No. of vowels: ",c)