#even
def is_even(num):
    return num%2==0
print(is_even(4))
print(is_even(9))
#str into int
str1="Hello"
str2="World"
result=str1+" "+str2
print(result)
#maximum of three numbers
def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(9,9,9,))
# count vowels
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("Hello World"))
#factorial of number
def factorial(n):
    