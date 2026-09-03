class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.d=[]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.d.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.d)==0:
            return -1
        self.d.pop(0)
        return True

    def Front(self) -> int:
        if len(self.d)!=0:
            return self.d[0]
        return -1

    def Rear(self) -> int:
        if len(self.d)==0:
            return -1   
        return self.d[-1]   

    def isEmpty(self) -> bool:
        if len(self.d)==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.d)==self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
