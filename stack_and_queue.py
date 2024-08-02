class Stack:
    """Stack obyekti"""
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        """Bo'sh ekanligini tekshirish"""
        return len(self.stack)==0
    
    def push(self,data):
        """Element qo'shish"""
        self.stack.append(data)
        return True
    
    def pop(self):
        """Element sug'urib olish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]

if __name__=='__main__':
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.stack)
    print("Popped element: ", stack.pop())
    print("Ustki element: ", stack.peek())
    print("Bo'shmi?: ", stack.isEmpty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

# Deque
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        return 'Queue is empty ! '

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        return 'Queue is empty ! '

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
print(queue.queue)

# class Node(object):
#     '''
#     Singly-linked list node for storing data in
#     a queue
#     '''
#     def __init__(self, data=None):
#         '''
#         Initialise a Node with optional data to be stored
#         '''
#         self.right = None
#         self.data = data
    
# class Queue(object):
#     '''
#     Queue structure implemented using a singly-linked list
#     '''
#     def __init__(self):
#         '''
#         Initialise an empty queue
#         '''
#         self.first = None
#         self.last = None

#     def enqueue(self, data):
#         '''
#         Enqueue data; putting it on the back of the queue
#         '''
#         new_node = Node(data)
#         if self.first is None and self.last is None:
#             # case 1: no nodes exist
#             self.first = new_node
#             self.last = self.first
#         else:
#             # case 2: at least one node exists
#             self.last.right = new_node
#             self.last = new_node
    
#     def dequeue(self):
#         '''
#         Dequeue data; removing it from the front of the queue
#         '''
#         if self.first is None:
#             # case 1: nothing on the queue
#             return None
#         else:
#             # case 2: something on the queue
#             data = self.first.data
#             next = self.first.right
#             if next is None:
#                 # case 1: nothing else queued
#                 self.first = None
#                 self.last = None
#             else:
#                 # case 2: something else queued
#                 self.first = next
#             return data

# # if __name__ == '__main__':
#     # Test the queue
# q = Queue()
# print (q.dequeue())
# q.enqueue(1)
# print (q.dequeue())
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')
# print (q.dequeue())
# q.enqueue('d')
# print (q.dequeue())
# print (q.dequeue())
# print (q.dequeue())
# print (q.dequeue())