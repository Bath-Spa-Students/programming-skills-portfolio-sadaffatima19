'''Write a Python program that uses the elif statement to determine the season based on the month provided as input.'''

spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]

month = input("Enter the month to know the season: ")

if month in spring:
  print("Its the spring season!")
elif month in summer:
  print("Its the spring summer!")
elif month in autumn:
  print("Its the autumn season!")
else:
  print("Its the winter season")
