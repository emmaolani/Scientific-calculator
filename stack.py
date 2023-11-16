class Input:
    def __init__(self, item):
        self.item = item
        self.negate = False
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, item):
        if self.is_empty():
            self.head = Input(item)
            self.size = self.size + 1
        else:
            new_node = Input(item)
            new_node.next = self.head
            self.head = new_node
            self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            old_list = self.head
            new_list = self.head.next
            self.head = new_list
            self.size = self.size - 1
            old_list.next = None
            return old_list.item

    def show_head(self):
        if self.is_empty():
            return None
        else:
            return self.head.item

    def show_list(self):
        if self.is_empty():
            return None
        else:
            head = self.head
            while head is not None:
                print(head.item)
                head = head.next

    def show_size(self):
        return self.size



