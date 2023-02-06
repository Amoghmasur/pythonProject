import time
class Demo:
    def printname(self):
        name=["raju","ramu","amogh"]
        for data in name:
            print(data)
            time.sleep(1)
    def printnum(self):
        for i in range(10):
            print(i)
            time.sleep(1)
    def add(self):
        a=10
        b=20
        c=a+b
        print("res is",c)
d=Demo()
d.printname()
d.printnum()

d.add()