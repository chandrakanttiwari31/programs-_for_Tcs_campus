

a=int(input("Enter your first number"))
b=int(input("Enter your second number"))


for i in range(a,b+1):
    rem=i
    sum=0
    while(rem!=0):
        sum=sum+(rem%10)**3
        rem=rem//10
    if(sum==i):
        print(i)
