'''You have given a Python list. Write a program to find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of an item.
Work with the given list: list1 = [5, 10, 15, 20, 25, 50, 20]'''

list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
  print(20)
  num = list1.index(20) #first occurence of 20
  list1[num] = 200
  print(list1)
