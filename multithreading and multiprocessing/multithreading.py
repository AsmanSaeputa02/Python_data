


import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')
        
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")



#create 2 thread

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

t = time.time()

# start the threds
t1.start()
t2.start()

# wait for the threds to complete
t1.join()
t2.join()

# print_number()
# print_letter()
finished_time=time.time()-t
print(finished_time)