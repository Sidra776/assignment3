"""Q# 01 Write a program that calculates the sum, difference, product, and average of three numbers"""
# Step 1: Get numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Step 2: Do the calculations
sum_result = num1 + num2 + num3
difference = num1 - num2 - num3
product = num1 * num2 * num3
average = sum_result / 3

# Step 3: Show the results
print("Sum is:", sum_result)
print("Difference is:", difference)
print("Product is:", product)
print("Average is:", average)


"""Q# 02 Write Python code to calculate the area of the following shapes


• Area=0.5×base×height
• Area=sidexside
• Area=π×radius2
• Area=length×width"""
# Triangle Area
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print("Area of Triangle:", triangle_area)

# Square Area
side = float(input("Enter side of square: "))
square_area = side * side
print("Area of Square:", square_area)

# Circle Area
radius = float(input("Enter radius of circle: "))
pi = 3.1416
circle_area = pi * radius * radius
print("Area of Circle:", circle_area)

# Rectangle Area
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print("Area of Rectangle:", rectangle_area)

"""Q# 03 Write a program to swap values of two variables"""
# Swapping two variables
a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
