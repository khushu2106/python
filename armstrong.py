num1 = int(input("Enter any number :"))
original = num1 
sum=0
while num1> 0:
    r = num1%10
    cube = r*r*r
    sum+=cube 
    num1 = num1//10
    if sum==original:
        print("Given number is armstrong number .")
    else:
       print(" Given number is not armstrong .")