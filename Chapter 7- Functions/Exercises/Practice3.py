'''Write a Python program that uses a function to check if a given number is prime or not.'''

def is_prime(number):
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count +=1
    if count == 2:
        print('The number {0} is the prime number.'.format(number))
    else:
        print('The number {0} is NOT the prime number.'.format(number))

  print(is_prime(2))
