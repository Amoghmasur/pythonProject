from time import time

def func1(a,b):
    #amogh
    return a+b
def func2(a,b):
    #anup
    num1=a
    num2=b
    if(a>b and a!=3):
        pass
    sum([4,3])
    return  a+b
if __name__=="__main__":
    init=time()
    for i in range(0,1000):
     func1(3,5)
    print("amogh time:",time()-init)
    init=time()
    for i in range(0,1000):
     func2(3,5)
    print("anup time:",time()-init)


#to print overall time remove print and add(print{"overall time:",time()-init}