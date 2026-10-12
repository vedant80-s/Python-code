# Question 4
# Question 2
try:

    with open("1c_python_task/file_and_Exception_handling_program/sample.txt" , 'r') as f:
        count = 0 
        while(f.readline()):
            count += 1
        print(count)
except Exception as e:
    print("Exxception Occur:-" , e.args)