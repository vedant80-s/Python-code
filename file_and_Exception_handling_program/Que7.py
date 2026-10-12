# Question 7
class CustomException(Exception):
    pass

try:
    raise CustomException("Custom Exception")
except CustomException as e:
    print("Exception:- ",e)
finally:
    print("Finally")