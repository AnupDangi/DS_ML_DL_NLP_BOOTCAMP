'''
Real World Example :Multiprocessing for CPU-bound tasks
Scenario :Factorial Calculation
Factorial Calculations,especially for large numbers,
involve significant computational work.Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores,improving performance.
'''


import multiprocessing
import math
import sys
import time

## Increase teh maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)


## function to compute factorial of a given number
def fact(number):
    result=math.factorial(number)
    print(f"result of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]  ## for calculating each factorial of each number it may take time so it takes time.
    start_time=time.time()
    
    with multiprocessing.Pool() as pool:
        results=pool.map(fact,numbers)
    
    end_time=time.time()
    
    print(f"Results:{results}")
    print(f"Time taken:{end_time-start_time} seconds")
    
    
