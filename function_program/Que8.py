# Question 8
def count_vowel(string):
    count = 0
    for i in string:
        if i in "aeiouAEIOU": count += 1      
    return count


string = "Hello Bishal"

print(count_vowel(string))

