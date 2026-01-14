#PYTHON PROGRAM TO CREATE SIMPLE CALCULATOR
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
opr = input("Enter a operator(+,-,*,/):")
if opr == '+':
  print("Addition is :",num1+num2)
elif opr == '-':
  print("Subtraction is:",num1-num2)
elif opr == '*':
  print("Multiplication is:",num1*num2)
elif opr == '/':
  if num2 == 0:
    print("Division not possible!!")
  else :
    print("Division is :",num1/num2)
else :
  print("Invalid operator!!!")
  