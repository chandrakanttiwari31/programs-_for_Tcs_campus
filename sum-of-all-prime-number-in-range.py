



a=int(input("Enter your starting number "))
b=int(input("Enter your last number "))


sum=0
for i in range(a,b+1):
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(i==j):
        sum=sum+i

print(sum)