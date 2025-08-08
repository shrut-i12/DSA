import time

n = int(input("Enter number of elements: "))

# Read elements into list
numbers = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    numbers.append(num)

# Read key to search
key = int(input("Enter element to search: "))

print(f"\nList: {numbers}")
print(f"Searching for: {key}")

# Linear search with timing
start_time = time.time()
position = -1
comparisons = 0

for i in range(n):
    comparisons += 1
    if numbers[i] == key:
        position = i
        break

end_time = time.time()

# Display result
if position != -1:
    print(f"Element found at position {position}")
else:
    print("Element not found")

# Time and case analysis
print(f"Comparisons made: {comparisons}")
print(f"Time taken: {(end_time - start_time) * 1000:.4f} milliseconds")

# Determine case
if position == 0:
    case = "Best case"
elif position == -1 or position == n-1:
    case = "Worst case"
else:
    case = "Average case"

print(f"This is: {case}")
print(f"Max possible comparisons: {n}")

