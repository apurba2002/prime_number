def prime(num):
    if (num == 1):
        res = False
    else:
        for i in range(2, num):
            if ((num % i == 0)):
                res = False
                break
            else:
                res = True
    return res
while True:
    numbers = prime(int(input("Enter a number :-")))
    if numbers == True:
        print("Prime number ")
        input("press enter for continue")
    else:
        print("Not a prime number .")
        input("press enter for continue")
