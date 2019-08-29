'''program for Palindrom  number which is given by user'''



a=int(input("Enter your number"))

rem=a
sum=0
while(rem!=0):
    sum=sum*10+(rem%10)
    rem=rem//10
if(sum==a):
    print(f" {a}  is palindrom number ")
else:
    print(f"{a}  is not palindrom number")