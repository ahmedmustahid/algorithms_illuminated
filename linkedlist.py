
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        nodelist=[]
        node = self.head
        while node is not None:
            nodelist.append(node.data)
            node = node.next
        nodelist.append("None")
        return "->".join(nodelist)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node=node.next 

    def add_first(self,node):
        node.next = self.head
        self.head = node

    
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self,targetnode, newnode):
        if self.head is None:
            raise Exception("Empty List")
        
        for current_node in self:
            if current_node.data==targetnode:
                newnode.next = current_node.next
                current_node.next = newnode
                return 
        
        raise Exception(f"{targetnode} is not in the list")

    #def add_before(self,targetnode,newnode):
    #    if self.head is None:
    #        raise Exception("Empty list")
    #    
    #    prevnode=self.head
    #    for current_node in self:
    #        print(f"current_node {current_node.data}")
    #        if current_node.data==targetnode:
    #            prevnode.next=newnode
    #            newnode.next=current_node
    #        prevnode=current_node

    #    raise Exception(f"{targetnode} not in the list")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception(f"{target_node_data} not in the list")

    
    def remove_node(self,targetnode_data):
        if self.head is None:
            raise Exception("Empty list")
        if self.head.data==targetnode_data:
            self.head = self.head.next
            return
        
        prevnode=self.head
        for current_node in self:
            if current_node.data==targetnode_data:
                prevnode.next = current_node.next
                return

            prevnode=current_node



if __name__=="__main__":
    ll1 = LinkedList(nodes=["a","b","c","d"])
    ll1.add_first(Node("first"))
    ll1.add_last(Node("last"))
    ll1.add_after("b",Node("after"))
    ll1.add_before("b",Node("before"))
    print(ll1)

    for l in ll1:
        print(l)

    



























