
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
        #nodelist.append("None")
        #return "->".join(nodelist)
        return " ".join(nodelist)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node=node.next 
    
    def __getitem__(self,nodenum):
        for i,node in enumerate(self):
            if i==nodenum:
                return node
    
    def __len__(self):
        return sum(1 for i in self)

    def __add__(self,other):
        if len(self) < len(other):
            ll_obj=self
        elif len(self) >= len(other):
            ll_obj=other
            other=self

        for i,node in enumerate(ll_obj):
            self.add_after(other[i].data,node)

        return self


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
    print(ll1[2])
    print("here") 
    for l in ll1:
        print(l)
    



    #ll1.add_first(Node("first"))
    #ll1.add_last(Node("last"))
    #ll1.add_after("b",Node("after"))
    #ll1.add_before("b",Node("before"))
    #print(ll1)

    #f = open("test_case1.txt","r")

    #for line in f:
    #    print(line)
    



























