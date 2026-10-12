# Question 2
try:

    with open("1c_python_task/file_and_Exception_handling_program/sample.txt" , 'r') as f:
        data = f.read()
        print(data)
except Exception as e:
    print("Exxception Occur:-" , e.args)