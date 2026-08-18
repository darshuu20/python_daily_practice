#even 
def is_even(num):
    return num%2==0
print(is_even(4))
print(is_even(3))
#concatenate
str1="Hello"
str2="World"
result=str1+" "+str2
print(result)
#maximum of three nums
def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(8,9,7))
#count of vowels
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("Hello World"))
#factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
#area of rectangle
def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(5,3))
#prime
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        return True
    print(is_prime(7))
    print(is_prime(10))
    #palindrome
    def is_palindrome(num):
        return str(num)==str(num)[::-1]
    print(is_palindrome(121))
    print(is_palindrome(123))
    #armstrong
    def is_armstrong(num):
        num_str=str(num)
        num_digits=len(num_str)
        return num==sum(int(digit)**num_digits for digit in num_str)
    print(is_armstrong(123))
    print(is_armstrong(153))
    
