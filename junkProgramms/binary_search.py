import time
def binary_search(input_array, value):
    n=1
    m=0
    while n!=0:
        arrlen=len(input_array)//(2*n)+m
        if input_array[arrlen]>value and arrlen!=len(input_array)-1:
            m=(arrlen+1)//2
        elif input_array[arrlen]<value and arrlen!=0:
            n=n+1
        elif input_array[arrlen]==value:
            return arrlen
        else:
            return -1
    return -1
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 30
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
