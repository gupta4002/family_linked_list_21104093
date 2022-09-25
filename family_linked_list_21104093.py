class Node:
    def __init__(self,name,age):
        self.name = name; 
        self.age=age; 
        self.previous = None;  
        self.next = None;  
          
class DoublyLinkedList:
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
           
    def addNode(self, name,age):  
        newNode = Node(name,age);  
           
        if(self.head == None):   
            self.head = self.tail = newNode;  
            self.head.previous = None; 
            self.tail.next = None;  
        else:  
            self.tail.next = newNode;  
            newNode.previous = self.tail; 
            self.tail = newNode; 
            self.tail.next = None;  

    def deleteNode(self, dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next is not None:
            dele.next.previous = dele.previous
        if dele.previous is not None:
            dele.previous.next = dele.next   

    def display(self):
         value_list=[]
         if(self.head != None): 
            current_node = self.head 
            while current_node.next != None: 
                value_list.append([current_node.name,current_node.age])
                current_node = current_node.next 
            value_list.append([current_node.name,current_node.age])
            print("Doubly linked list of family: "); 
            print(value_list)
         else: 
            print("No node")
            return False

    def displayRev(self):  
        value_list=[]
        current = self.tail;  
        if(self.tail == None):  
            print("List is empty");  
            return;  
        else:
            print("Doubly linked list of family in reverse: ");  
            while(current != None):  
                value_list.append([current.name,current.age])
                current = current.previous;  
            print(value_list)
              
dList = DoublyLinkedList(); 
dList.addNode("Garvit",17);  
dList.addNode("Garima",17);  
dList.addNode("Noori",39);  
dList.addNode("Pankaj",42); 
dList.display();  
dList.displayRev(); 
dList.deleteNode(dList.head.next.next); 
print("After deleting from middle ")
dList.display(); 