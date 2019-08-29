'''program for reverse the number which is given by user'''



a=int(input("Enter your number"))

rem=a
sum=0
while(rem!=0):
    sum=sum*10+rem%10
    rem=rem//10
print(sum)