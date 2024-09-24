class MyQueue:

    def __init__(self):
        self.queue=[]
        self.cnt=0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.cnt+=1

    def pop(self) -> int:
        n=len(self.queue)
        for i in range(n-1):
            self.queue[i],self.queue[i+1]=self.queue[i+1],self.queue[i]
        self.cnt-=1
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.cnt==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()