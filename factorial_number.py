'''program for calculating the Factorial by given number'''

a=int(input("Enter your number"))
fact=1
for i in range(2,a+1):
    fact=fact*i
print(f"your factorial number is {fact}")