def merge_sort(array):
    print("the array passed to the function")
    print(array)
    if len(array)>1:
        left=array[:len(array)//2]
        right=array[len(array)//2:]
        print("this is the array after spliting is in two")
        print(f"LEFT: {left}",f"RIGHT: {right}")
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        print(f"recursive calls to the merge_sort function done, the current array slice is {array}")
        while i<len(left) and j<len(right):
            print("i am going to print the left and the right ")
            print(f"LEFT: {left}",f"RIGHT: {right}")
            if left[i]>right[j]:
                print(f"comparing between {left[i]} and {right[j]}")
                array[k]=left[i]
                i=i+1
            else:
                print(f"else block {left[i]} and {right[j]}")
                array[k]=right[j]
                j=j+1
            print("the initial array after change ")
            print(array)
            k=k+1
        while i<len(left):
            print("continue the left part")
            array[k]=left[i]
            print(array)
            i=i+1
            k=k+1
        while j<len(right):
            print("continue the right part")
            array[k]=right[j]
            j=j+1
            k=k+1
lis=[12, 11, 13, 5, 6, 7]
merge_sort(lis)
#lis=[2,4,1]
#merge_sort(lis)
