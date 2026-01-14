#CHECK WHETHER THE YEAR IS LEAP OR NOT
year = int(input("Enter the year of your choice:"))
if (year%4==0 and year%100!=0 ) or (year%400==0):
    print(year,"is not a leap year")
else :
    print(year,"is not a leap year")
    