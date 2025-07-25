my_list=[1,2,2,3,4,4,4,5]
print("occurrens of each elements")
for item in set(my_list):
    print(item,"occurs",my_list.count(item),"times")
unique_list=list(set(my_list))
print("list after removing duplicates:",unique_list)


