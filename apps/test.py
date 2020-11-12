def sort_array(arr):
    sorted_arr = [8, 2, 5, 4, 29, 6, 7, 45, 9]



    x = len(sorted_arr)
    for i in range(x):
        for y in range(1,x):
            if sorted_arr[y-1] > x[y]:
                (sorted_arr[y-1], sorted_arr[y]) = (sorted_arr[y], sorted_arr[y-1])
    return sorted_arr
    
