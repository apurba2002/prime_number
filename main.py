num = int(input("Enter a number :-"))
i = 2
prime =""
for i in range(2,num):
    if ( (num%i)==0):
        prime = "no"
    else:
        prime = "yes"
if (prime == "no"):
    print(" a prime number")
    input()
elif(num==1):
    print("prime number")
    input()
else:
    print("Not a prime number")
    input()
