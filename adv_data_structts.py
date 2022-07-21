from collections import deque

class Stack:
    
    def __init__(self, data = None):
        self.stack = list(data)
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack) > 0:
            return(self.stack[len(self.stack) - 1])
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    
    

class Queue(deque):
    
    def __init__(self, data = None):
        self.queue = deque(data)
        
    def push(self, item):
        self.queue.append(item)
        
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        
    def peek(self):
        if len(self.queue) > 0:
            return(self.queue[len(self.queue) - 1])
        else:
            return None
        
    def __str__(self):
        return str(self.queue)
    



class MaxHeap:
    
    def __init__(self, items = []):
        #taking on list methods
        #will create a heap list
        super().__init__()
        
        #we insert zero in the heap because heaps start at 1
        self.heap = [0]
        for item in items: 
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
            
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
        
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
            
        else:
            max = False
        return max
    
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __floatUp(self, index):
        parent = index //2
        if index <- 1:
            return 
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
            
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
            
    def __str__(self):
        return(self.heap)
    



class Node:
    
    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    def __str__(self):
        return ('(' + str(self.data) + ')')
    
class LinkedList:
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False
    
    def print_linked_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end= '->')
            this_node = this_node.next_node
        print('None')
        
        
        

class CircularLinkedList:
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1
        
    
    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node
            
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while True:
            if this_node == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                    
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node
            
    def print_list(self):
        
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end= '->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end= '->')
        print()
        
        


class DoubleLinkedList:
    
    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0
        
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1
        
    
    def find(self, d):
        
        
    
    
