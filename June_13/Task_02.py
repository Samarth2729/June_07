# Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
#Equilateral Triangle: All three sides have the same length.
# Isosceles Triangle: Two sides are equal.
# Scalene Triangle: None of the sides are equal

side1 = float(input("Enter the side 1\n"))
side2 = float(input("Enter the side 2\n"))
side3 = float(input("Enter the side 3\n"))
if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")