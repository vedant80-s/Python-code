# Question 4
def prime_or_not(num , i = 2) -> bool:
    if num == 1 : return False
    if i == num: return True
    if num % i == 0:return False
    return prime_or_not(num , i + 1)


print(prime_or_not(9))