def merge_sort(nums):
    # Base case
    if len(nums) <= 1:
        return nums
    
    # Divide

    middle = len(nums) // 2
    left_list = nums[:middle]
    right_list = nums[middle:]

    merge_sort(left_list)
    merge_sort(right_list)

    # Conquer

    # The i index is for the left_list, it is pointing
    # to the current index of the left_list
    i = 0
    # The j index is for the right_list, it is pointing
    # to the current index of the right_list
    j = 0
    # The k index is for the nums list, it is pointing
    # to the current index of the nums list
    k = 0

    #Here we will compare the current index of the left_list
    #with the current index of the right_list (the values on each index)
    while i < len(left_list) and j < len(right_list):
        # If the value on the left_list is lower, we set that value
        # to the nums list
        # and increment the i index
        if left_list[i] < right_list[j]:
            nums[k] = left_list[i]
            i += 1
        else:
            # If the value on the right_list is lower, we set that value
            # to the nums list
            # and increment the j index
            nums[k] = right_list[j]
            j += 1
        
        # Increment the k index because
        # we set a value on the nums list in the if/else statements above
        k += 1
    
    #After we do the while loop above, we will have some values left
    #on either the left_list or the right_list
    #We need to add those values to the nums list
    #This is for the left_list
    while i < len(left_list):
        nums[k] = left_list[i]
        i += 1
        k += 1
    
    #This is for the right_list
    while j < len(right_list):
        nums[k] = right_list[j]
        j += 1
        k += 1

A = [38, 27, 43, 3, 9, 82, 10]
B = [ 5, 2, 7, 6, 2, 1, 0, 3, 9, 4]

merge_sort(A)
merge_sort(B)
print(A)
print(B)