num1=int(input("Enter the values1:-"))
num2=int(input("Enter the values2:-"))
opr=input("Enter the Opr..(+,-,*,/)")
if opr=="+":
    print(num1+num2)
if opr=="-":
    print(num1-num2)
    if opr=="*":
        print(num1*num2)
        if opr=="/":
            print(num1/num2)
        else:
            print("Invalid operators..")