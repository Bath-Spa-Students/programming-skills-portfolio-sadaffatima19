'''Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.'''

def area(radius):
  area = 3.14*radius**2
  return area

radius = float(input("Enter the radius of the circle: "))  
print ("The area of the circle is: ", area(radius))
