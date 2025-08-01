import time

def liner_time(n):
    print(f"\nO(n) for n = {n}")
    start = time.time()
    for i in range(n):
        pass # Simulate some work
    end = time.time()
    print(f"Time taken : {end - start:.6f} seconds")   
liner_time(100)
liner_time(200)
liner_time(300)
