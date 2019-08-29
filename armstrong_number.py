'''program for armstrong the number which is given by user'''



a=int(input("Enter your number"))

rem=a
sum=0
while(rem!=0):
    sum=sum+(rem%10)**3
    rem=rem//10
if(sum==a):
    print(f" {a}  is Armstrong number ")
else:
    print(f"{a}  is not Armstrong number")