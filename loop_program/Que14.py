# Question 14
num = int(input("Enter Number:- "))
power = int(input("Enter Power:- "))

power1 = num
# Normal Way
for i in range(1,power):
    power1 *= num


if power == 0:
    power1 = 1
print("Power of {} is {}".format(num , power1))


# Special Python Way
power = num**power
print("Power of {} is {}".format(num , power))
