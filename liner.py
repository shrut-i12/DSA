def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
          return i
    return -1
arr =[5,12,7,9,23,18]
target=23       
result = linear_search(arr,target)
if result!=-1:
   print(f"element {target} found at index {result}")
else:
    print(f"element{target} not found in the list")  

