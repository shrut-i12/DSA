import time

def exponential_time(n):
    print(f"\nO(2^n) for n = {n}")
    def helper(k):
        if k == 0:
            return
        helper(k - 1)
        helper(k - 1)
    
    start = time.time()
    helper(n)
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

exponential_time(10)
exponential_time(30)
exponential_time(40)