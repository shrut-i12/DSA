import time

# Predefined data
lst = sorted([15, 7, 22, 3, 10, 18])
key = 10

print("Sorted list:", lst)
print(f"Searching for: {key}")

# Binary search with timing
start_time = time.time()
start, end, steps = 0, len(lst) - 1, 0

while start <= end:
    steps += 1
    mid = (start + end) // 2
    
    if lst[mid] == key:
        print(f"Found {key} at position {mid}")
        break
    elif lst[mid] < key:
        start = mid + 1
    else:
        end = mid - 1
else:
    print("Not found")

end_time = time.time()

# Results
print(f"Steps taken: {steps}")
print(f"Time taken: {(end_time - start_time) * 1000:.4f} milliseconds")

# Determine case
max_steps = len(lst).bit_length() - 1
if steps == 1:
    case = "Best case"
elif steps >= max_steps:
    case = "Worst case"
else:
    case = "Average case"

print(f"This is: {case}")
print(f"Max possible steps: {max_steps}")
