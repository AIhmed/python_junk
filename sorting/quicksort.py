def quickSort(array):
    if len(array)==1:
        return array
    quicksort(array)
    pivot=len(array)-1
    #the pivot will be initilized to take the last value of each slice 
    #after selecting the pivot 
    #we compare the pivot with the other values in the slice 
    #we call the function back to reselect the pivot that is the last element in the slice 
    if i in range(0,pivot):
        if array[i]>array[pivot]:
            array[i],array[pivot]=array[pivot],array[i]

