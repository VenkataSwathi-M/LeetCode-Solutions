class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack1.append(val)
        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)
    def pop(self):
        """
        :rtype: None
        """
        if self.stack1:
            val = self.stack1.pop()
            if val == self.stack2[-1]:
                self.stack2.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1] if self.stack1 else null

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1] if self.stack2 else null


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
