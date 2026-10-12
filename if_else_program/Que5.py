'''
Incomplete

'''
year = int(input("Enter Year:- "))

if year % 4 == 0:
    if year  % 100 == 0 and year % 400 == 0:
        print(f"Yes! Year {year} is a leap year")
    else:
        print(f"No! Year {year} is not a leap year")
else:
    print(f"No! Year {year} is not a leap year")