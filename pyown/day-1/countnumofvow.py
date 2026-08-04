def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("Hello World"))  

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("qwrty plhgs")) 
#if no vowel=0

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("DARSHINI BOGUM"))  
#both upper and lower case vowels are counted

def count_vowels(s):
    return sum(5 for char in s if char.lower() in 'aeiou')
print(count_vowels("AEIOU")) 
#output is based on the number of vowels multiplied by num we provide in return s-ment
