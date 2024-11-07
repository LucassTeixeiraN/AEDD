from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, site_name, link):
        new_node = Node(site_name, link)
        new_node.next = self.head
        self.head = new_node

    def searchAndMove(self, site_name):
        current = self.head
        previous = None
        
        while current is not None:
            if current.site_name == site_name:
                if previous is None:
                    return current.link  
                
                if previous is not None:
                    previous.next = current.next 
                current.next = self.head  
                self.head = current
                
                return current.link  
            
            previous = current
            current = current.next
        
        return None

    def display(self):
        current = self.head
        while current is not None:
            print(f'Site: {current.site_name}, Link: {current.link}')
            current = current.next
