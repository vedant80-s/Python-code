import numpy as np 

student_and_marks = np.random.randint(33,100,(30,5))

print("                                 ==== Student Score Analysis ==== ")

print("             ==== Total ==== ")
print(np.sum(student_and_marks , axis=1))
print("             ==== Average ==== ")
print(np.average(student_and_marks , axis=1))