class cal:
    num=2
    def __init__(self,a,b):
        self.fnumber=a
        self.snumber=b
        print("i am constructor,call automatically when object will be created")
    def add(self):
       re=self.fnumber+self.snumber+self.num
       print(re)
    print("this is number displaying")

obj=cal(2,2)
obj.add()
print(obj.num)