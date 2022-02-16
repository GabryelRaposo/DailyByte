'''This is an example to understand on how linked Lists works on software development
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self,data):
        if self.head: #In this condition, there are elements already in the list, this way
            #Its necessary to pass through all elements, and add the new data in the final.
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next 
            pointer.next = Node(data)
        else: #In this condition, there aren't elements on the list, the data will be store on the head.
            self.head = Node(data)

        self._size = self._size + 1
         
    def __len__(self):
        return self._size
    
    def __getitem__(self,index): #sobrecarga de operador.
        pointer = self.head

        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list out of range')
        if pointer: #verifying if the index == len(list) which is out of index.
            return pointer.data #pointer is a node object. thus, its correctly call the argument data
        raise IndexError('list out of range')

    def __setitem__(self,index, data):
        pointer = self.head

        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list out of range')
        if pointer: #verifying if the index == len(list) which is out of index.
            pointer.data = data  #substituting the data to a new index
        else:
            raise IndexError('list out of range')

    def index(self, elem):
        pointer = self.head
        index = 0
        while(pointer.next):
            if pointer.data == elem:
                return index
            pointer = pointer.next
            index = index + 1
        else:
            raise ValueError(f'The element {elem} is not in the list')  

    def lenght(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0

        while current_node:
            total +=1
            current_node = current_node.next
            return total

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def display(self):
        contents = self.head

        if contents is None:
            print("The list has no elements")
        while contents:
            print(contents.data)
            contents = contents.next
        print("-----------") 

    def reverse_linkedlist(self):
        prior_node = None
        current_node = self.head

        while current_node != None:
            next = current_node.next
            current_node.next = prior_node
            prior_node = current_node
            current_node = next
        self.head = prior_node

lista1 = LinkedList()
lista2 = LinkedList()  
def merge_list(self,head1,head2):
    dummy = Node(data=None)
    tail = dummy
    
    while True:
        if head1.data < head2.data:
            tail.next = head1.data
            



    pass



mylist = LinkedList()
mylist.display()
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.display()
#mylist.to_list()
print(len(mylist))
print(mylist[2])

for i in mylist:
    print(i)