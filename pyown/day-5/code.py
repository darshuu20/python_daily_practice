#even
def is_even(num):
    return num%2==0
print(is_even(4))
print(is_even(5))
#concatenate two str
str1="Hello"
str2="World"
result=str1+" "+str2
print(result)
#Maximum of three
def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(1,2,3))
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
#str to int
str_num="12345"
int_num=int(str_num)
print(int_num)
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
        return num==sum(int(digit)**num_digits for digits in num_str)
    print(is_armstrong(123))
    print(is_armstrong(153))
    #leap year
    def is_leap_year(year):
        return (year%4==0 and year%100==0)and (year%400!=00)
    print(is_leap_year(2020))
    print(is_leap_year(2024)) 
    #fibonacci
    def fibonacci(n):
        sequence=[0,1]
        for i in range(2,n):
            sequence.append(sequence[-1]+sequence[-2])
            return sequence[:n]
        print(fibonacci(7))
         #decimal to binary
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]
    print(decimal_to_binary(10))
    