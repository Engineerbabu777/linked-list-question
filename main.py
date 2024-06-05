class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.undo_stack = Stack()

    def save_state(self):
        current = self.head
        state = []
        while current:
            state.append(current.data)
            current = current.next
        self.undo_stack.push(state)

    def restore_state(self):
        state = self.undo_stack.pop()
        if state is None:
            return
        self.head = None
        for data in state:
            self.append(data)

    def append(self, data):
        self.save_state()
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, position, data):
        self.save_state()
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        self.save_state()
        if self.head is None:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of bounds")
            current = current.next
        current.next = current.next.next

    def move_line(self, j, k):
        self.save_state()
        if j == k:
            return
        prev_j, node_j = self._get_node_at_position(j)
        prev_k, node_k = self._get_node_at_position(k)
        if prev_j:
            prev_j.next = node_j.next
        else:
            self.head = node_j.next
        if prev_k:
            node_j.next = node_k.next
            node_k.next = node_j
        else:
            node_j.next = self.head
            self.head = node_j

    def replace_text_in_line(self, n, old_text, new_text):
        self.save_state()
        node, _ = self._get_node_at_position(n)
        if node:
            print("1")
            node.data = new_text
        else:
            raise IndexError("Position out of bounds")

    def _get_node_at_position(self, position):
        current = self.head
        prev = None
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of bounds")
            prev = current
            current = current.next
        return prev, current

    def move_next(self, current):
        if current and current.next:
            return current.next
        return None

    def move_previous(self, current):
        prev = None
        temp = self.head
        while temp and temp != current:
            prev = temp
            temp = temp.next
        return prev
    
    def view(self):
        current = self.head
        line_number = 0
        while current:
            print(f"{line_number}: {current.data}")
            current = current.next
            line_number += 1

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

def read_file_to_linked_list(file_path):
    linked_list = LinkedList()
    with open(file_path, 'r') as file:
        for line in file:
            linked_list.append(line.strip())
    return linked_list

def main():
    file_path = 'myfile.txt'  # Replace with your text file path
    linked_list = read_file_to_linked_list(file_path)
    
    print("Reading from file...")
    linked_list.view()
    print("-----------------------------------------")

    obj = LinkedList()
    obj.insert_at_position(0,"0 point!")
    obj.insert_at_position(1,"1 point!")
    obj.insert_at_position(2,"2 point!")
    obj.insert_at_position(3,"3 point!")
    obj.insert_at_position(4,"4 point!")
    
    obj.delete_at_position(2)
    
    obj.replace_text_in_line(2, "2 point!", "new_text")
    obj.view()
    print('By craeting an intance')
    obj.view()
    print('-----------------------')
    # obj.move_line(1, 3)
    
    
    # obj.delete_at_position(3)
    # obj.move_line(1, 4)
    obj.replace_text_in_line(2, "old_text", "new_text")
    
    
    
    print('By replacing 2"\s text')
    obj.view()
    print('-----------------------')
    
    # linked_list.view()
    
    # Move to next and previous lines
    # current = linked_list.head
    # print(current.data)
    # current = linked_list.move_next(current)
    # current.data
    # current = linked_list.move_previous(current)
    # current.data
    
    # Undo the last operation
    obj.restore_state()
    obj.view()
    

if __name__ == "__main__":
    main()