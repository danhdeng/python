from functools import cache
import time

# @cache
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) +fib(n-2)

def main():
    start=time.perf_counter()
    for i in range(40):
        print(i, fib(i))
    print("done")
    elapsed= time.perf_counter() -start
    print(f"completed in {elapsed} seconds")
        

if __name__ == '__main__':
    main()
    
    