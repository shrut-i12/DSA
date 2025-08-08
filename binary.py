lst=sorted([15,7,3,10,18])
key=18
low,high,steps=0,len(lst)-1,0
while low<=high:
    steps+=1
    mid=(low+high)//2
    if lst[mid]==key:
        print(f"found {key} at position {mid} ")   
        break
    elif lst[mid]<key:
        low=mid+1
    else:
        high=mid-1
else:
    print("not found")
print("sorted list:",lst)
print("steps taken:",steps)            
