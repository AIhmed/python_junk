import time
def fib(position):
    if position==0:
        print('returning 0')
        return 0
    elif position==1:
        print('returning 1')
        return 1
    else:
        print(f"the position we are at is {position}")
        result=fib(position-1)+fib(position-2)
        print(f"the result is {result}")
        return result
print(fib(4))
#print(fib(8))
#print(fib(9))

