'''Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.'''

num_list = []
while True:
  num = float(input("Enter the numbers (0 to exit): "))
  num_list.append(num)
  max_num = 0
  min_num = 0
  if num == 0:
    break
print("The maximum number is: ", max(num_list))
print("The minimum number is:", min(num_list))
