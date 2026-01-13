#PYTHON TO FIND AREA OF CIRCLE , RECTANGLE , SQAURE ,TRIANGLE
#1ST AREA OF CIRCLE:
print("Let's fid the area of circle!!!")
radius = float(input("Enter the radius : "))
pi = 3.14
area_circle = pi*radius*radius 
print("Here is the area of circle:",area_circle)

#2ND AREA OF RECTANGLE :
print("Let's find the area of rectangle!!!")
length = float(input("Enter the lenght of rectangle:"))
breadth  = float(input("Enter the breadth of rectangle:"))
area_rect = length * breadth
print("Here is the area of rectangle:",area_rect)

#3RD AREA OF SQUARE :
print("Let's find the area of square!!!")
side = float(input("Enter the measurement of side of square :"))
area_sqr = side*side
print("Area of square : ",area_sqr)

#4TH AREA OF TRIANGLE:print("Let's find the area of triangle!!!")
base = float(input("Enter the base measurement :"))
height = float(input("Enter the height:"))
area_tri = 0.5*base*height
print("Area of triangle:",area_tri)
