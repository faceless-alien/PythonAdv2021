class Stack():
    def __init__(self, items):
        self.items=items
    def append(self, item):
        i=[item]
        self.items = i+self.items
    def pop(self):
        self.items = self.items[1:]
    def peak(self):
        return self.items[0]
class Queue():
    def __init__(self,items):
        self.items = items
    def append(self, item):
        i=[item]
        self.items = i+self.items
    def pop(self):
        self.items = self.items[:-1]
    def peak(self):
        return self.items[-1]
        