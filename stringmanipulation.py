str="PyThOn"
lower=[]
upper=[]
for i in str:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
str="".join(lower+upper)
print(str)