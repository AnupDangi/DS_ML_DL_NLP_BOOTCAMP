## Multithreading
## When to use Multi Threading

## I/O bound task :Tasks that spend more time waiting for I/O Operations (e.g., file operations)
## Concurrent Execution :When you want to improve the throughput of your application


import threading
import time

## Single Threaded
# def s_thread_print_numbers():
#     for i in range(5):
#         time.sleep(2) ## think as io operation
#         print(f"Number:{i}")
        


# def s_threadprint_letter():
#     for letter in "abcde":
#         time.sleep(2) ## think as io operation
#         print(f'Letter in :{letter}')
        

# t=time.time()
# s_thread_print_numbers()
# s_threadprint_letter()
# finished_time=time.time()-t
# print(finished_time)


## Multithreading
def m_thread_print_numbers():
    for i in range(5):
        time.sleep(2) ## think as io operation
        print(f"Number:{i}")
        


def m_threadprint_letter():
    for letter in "abcde":
        time.sleep(2) ## think as io operation
        print(f'Letter in :{letter}')
        
## Create 2 threads
t1=threading.Thread(target=m_thread_print_numbers)
t2=threading.Thread(target=m_threadprint_letter)

t=time.time()
t1.start()
t2.start()

## Wait for threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)




