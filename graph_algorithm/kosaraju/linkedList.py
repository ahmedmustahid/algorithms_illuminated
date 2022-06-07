class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.explored = False
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0)) 
            self.head = node

            for element in nodes:
                node.next = Node(data= element)
                node = node.next

    def __repr__(self) -> str:
        
        node = self.head

        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append('None')
        return '->'.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def addFirst(self, node):
        node.next = self.head
        self.head = node

    def addLast(self, node):
        if self.head is None:
            self.head = node
            return
        for currentNode in self:
            pass
        currentNode.next = node

    def addAfter(self, targetNodeData, newNode):
        if self.head is None:
            raise Exception('List is empty')

        for currentNode in self:
            if currentNode.data == targetNodeData:
                newNode.next = currentNode.next
                currentNode.next = newNode
                return
        raise Exception(f"Node with {targetNodeData} not found")

    def addBefore(self, targetNodeData, newNode):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == targetNodeData:
                newNode.next = node
                previousNode.next = newNode
                return

            previousNode = node
        raise Exception(f"{targetNodeData} does not exist in the list")

if __name__=="__main__":
    
    myList = [1, 2, 3, 4]
    lList = LinkedList(nodes=myList)
    print(lList)

    lList.addAfter(3, Node(data=6))
    print(lList)


        