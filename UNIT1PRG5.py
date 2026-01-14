#PROGRAM TO FIND FACTORIAL OF A NUMBER :
num = int(input("Enter the number:"))
fact = 1
for i in range (1,num+1):
    fact = fact * i
    print("Factorial:",fact)

#WAP TO FIND SQUARE AND CUBE OF A NUMBER:
print("SQUARE AND CUBE OF A NUMBER")
number = int(input("Enter the number:"))
print("Square:",number**2)
print("Square:",number**3)
