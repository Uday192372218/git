Lower=eval(input("enter a Lower range" ))
upper=eval(input("enter a upper range" ))
for n in range(Lower , upper+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
            else:
                print(n)
