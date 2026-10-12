# Question 2
try:

    with open("1c_python_task/file_and_Exception_handling_program/sample.txt" , 'a+') as f:
        f.write("\nBhai Append Kiya hai Text Ko")
        f.seek(0)
        data = f.read()
        print(data)
except Exception as e:
    print("Exxception Occur:-" , e.args)