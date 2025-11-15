class Node:
    """
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
  
class BinarySearchTree:
    """
    """
    def __init__(self):
        self.root = None
  
    def is_empty(self):
        """
        """
        return self.root is None
    
    def insert(self, key):
        """
        """
        node = Node(key)
        if self.is_empty():
            self.root = node
        else:
            current = self.root
            parent = None

            while current:
                parent = current
                if key == current.key:
                    raise Exception('Key already exist')

                if key < current.key:
                    current = current.left
                    
                elif key > current.key:
                    current = current.right
            
            if key < parent.key:
                parent.left = node

            elif key >= parent.key:
                parent.right = node
                
              
    
    def search(self, key):
        """
        """
        current = self.root
        
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            
        return False
            
