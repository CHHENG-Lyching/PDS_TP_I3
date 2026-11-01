#Problem 7. Digit Tools  
def digit_sum(n):
    n = abs(n)
    total = 0
    while n>0:
        total += n % 10 
        n //= 10     #drop the last digit
    return total

def reverse_number(n):
    r = 0
    while n>0:
        r = r * 10 + n % 10
        n //= 10
    return rvs

def palindrome(n):
    return n  == reverse_number(n)    #number that stays the same when its digits are reversed


print()
for n in [2026, 12321, 9875]:
    print(n,": digit sum = ", digit_sum(n),", reverse = ",  reverse_number(n), ", palindome = ", palindrome(n))