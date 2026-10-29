import numpy as np 
import time as t 

num = 100000
st = t.perf_counter_ns()
li = [i for i in range(num)]
print("Python List Time:",(t.perf_counter_ns() - st))

arr = np.arange(num)
st = t.perf_counter_ns()
print("Numpy Array Time:",(t.perf_counter_ns() - st))