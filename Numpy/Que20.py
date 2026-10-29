import numpy as np 
arr = np.random.randint(1 , 100 , (30,5))
print("====Student Marks Analyzer====")
avg = np.average(arr , axis=1)
print("Total:\n",np.sum(arr , axis=1))
print("Average:\n",avg)
print("Pass Count:",avg[avg > 33].size)
print("Topper:", np.argmax(avg))