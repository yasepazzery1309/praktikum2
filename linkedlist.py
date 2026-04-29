class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambah di akhir
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Menambah di awal
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Menambah setelah nilai tertentu
    def insert_after(self, target_data, new_data):
        current = self.head
        while current and current.data != target_data:
            current = current.next
        
        if current:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node

    # Representasi string untuk print(ll)
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

# Kode kamu sekarang bisa berjalan:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.insert_after(20, 25)

print(ll)