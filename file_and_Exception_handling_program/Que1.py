# Question 1
try:
    print("Line 2")
    with open("python/1c_python_task/file_and_Exception_handling_program/sample.txt" , "w+") as f:
        f.write("Hello Bhai Kya Haal Hai ? ")
        f.seek(0)
        data = f.read()
        print(data)
except Exception as e:
    print("Exception Occur:-", e.args)