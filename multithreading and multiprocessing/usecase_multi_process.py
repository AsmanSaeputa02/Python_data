

import  multiprocessing
import math
import sys 
import time


# Increase the max number of digits fo integer conversation
sys.set_int_max_str_digits(100000)

## function to compute factorial  of a given nymber

def computer_factorialnumber(number):
    print(f"Computer factorial of {number}")
    result = math.factorial(number)
    return result
if __name__=="__main__":
    numbers=[5000,6000,4000,8000]
             
    start_time=time.time()

    ## create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorialnumber,numbers)


    end_time=time.time()

    print(f"Results:{results}")
    print(f"Time taken: {end_time - start_time}  seconds")



