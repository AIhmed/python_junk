def vector_sum(vector):
    if isinstance(vector,list):
        if len(vector)>1:
            left=vector[:(len(vector)//2)]
            right=vector[len(vector)//2:len(vector)]
            print(right)
            print(left)
            vector_sum(left)
            vector_sum(right)
        else:
            print("\n")
array=[0,4,8,11,1,2]
var=vector_sum(array)
print(var)
