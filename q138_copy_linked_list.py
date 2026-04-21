class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        #step 1, traverse the linked list and clone all the nodes
        cloned_nodes = {}
        current = head
        while current is not None:
            #cloning step
            new_node = Node(current.val)
            #storing step
            cloned_nodes[current] = new_node
            #moving forward
            current = current.next
        current = head
        #step 1 completed
        #step 2, wiring all the pointers
        '''while current is not None:
            #parse the dictionary you created earlier
            copy = cloned_nodes[current]
            #assign next and random ptrs to "copy"
            if(current.next is not None):
                copy.next = cloned_nodes[current.next]
            else: copy.next = None
            if(current.random is not None):
                copy.random = cloned_nodes[current.random]
            else: copy.random = None
            #parsing while loop
            current = current.next
            '''
        #simplified step 2
        while current:
            copy = cloned_nodes[current]
            copy.next = cloned_nodes.get(current.next)
            copy.random = cloned_nodes.get(current.random)
            current = current.next
        
        #step 3, return head of cloned list
        return cloned_nodes[head]