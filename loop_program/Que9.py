# Question 9
num = int(input("Enter number:- "))

fir = 0 
sec = 1 

for i in range(1 , num+1):
    print(fir,"",sep=" " , end="")
    fir , sec = sec ,(fir + sec)

