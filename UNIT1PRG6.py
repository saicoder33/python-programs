#WRITE A PYTHON PROGRAM TO SWAP TWO NUMBERS WITHOUT USING 3RD VARIABLE
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
print("Numbers before swapping:")
print("Num1:",num1)
print("Num2:",num2)
num1,num2=num2,num1
print("Numbers after swapping:")
print("Num1:",num1)
print("Num2:",num2)