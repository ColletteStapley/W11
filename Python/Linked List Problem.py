from hashlib import new
from os import remove


class Chain:
    """
    Implement the LinkedList data structure. right below is an inner class called
    Link.  An inner class means that its real name is related to 
    the outer class.  To create a Link object, we will need to 
    specify Chain.Link
    """

    class Link:
        """
        Each link of the Chain(aka Linked List) will have data and links to the 
        previous and next link. 
        """

        def __init__(self, data):
            """ 
            Initialize the link to the data provided. At the start, the individual
            link is alone, so it isn't connected to anything.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty chain/linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new link at the front (i.e. the head) of the
        chain.
        """
        # Create the new node
        new_link = Chain.Link(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_link
            self.tail = new_link
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_link.next = self.head # Connect new link to the previous head
            self.head.prev = new_link # Connect the previous head to the new link
            self.head = new_link      # Update the head to point to the new link
    

    #############################
    #    Here is the Problem    #
    #############################
    def find_duplicates(self):
        """
        Search thorught the linked list and return all the duplicates
        """
        
        return 0
    ############################
    #    End of the Problem    #
    ############################


# Now for the test Cases
print("\n~~~~~~~~~~~~~~~~~|| Find Duplicates Test ||~~~~~~~~~~~~~~~~~~~")
chain = Chain()
chain.insert_head(2)
chain.insert_head(4)
chain.insert_head(17)
chain.insert_head(1)
chain.insert_head(5)
chain.insert_head(8)
chain.insert_head(2)
chain.insert_head(9)
chain.insert_head(3)

print(chain.find_duplicates()) # [2]

chain.insert_head(9)
chain.insert_head(3)

print(chain.find_duplicates()) # [2, 3, 9]