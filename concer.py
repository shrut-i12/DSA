def divide_and_conquer(list):
    if len(list) <= 1:
        print("Base case",list)
        return
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]
    print