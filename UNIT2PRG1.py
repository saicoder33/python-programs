#WRITE A PYTHON PROGRAM TO PRINT LARGEST NUMBER OUT OF THREE
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
if num1 > num2 :
    if num1 > num3 :
        print("Largest number is :",num1)
    else :
        print("Largest number is:",num2)
else :
    print("Largest number is :",num3)



