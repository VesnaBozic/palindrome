class Queue:
    def __init__(self):
        self.items = []


    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def __str__(self):
        return str(self.items)