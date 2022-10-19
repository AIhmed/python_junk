def bubble(array):
    flag=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]<array[j]:
                print(f"permuting between {array[i]} and {array[j]}")
                array[i],array[j]=array[j],array[i]
    return array
lis=[88,7,9,90,44,234,12,87,21]
sorted_list=bubble(lis)
print(sorted_list)

