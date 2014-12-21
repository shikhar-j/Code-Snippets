class ListElem:
   def __init__(self, next, value):
       self.next = next
       self.value = value


class List:
    def __init__(self):
        self.head = ListElem(None, None)
        self.current = self.head

    def get(self):
        return self.current.value;

    def reset(self):
        self.current = self.head

    def next(self):
        if self.current.next:
            self.current = self.current.next
        
        return self.current.value

    def insert(self, value):
        if self.head.value:
            elem = ListElem(None, value)
            self.current.next = elem
            self.current = self.current.next
        else:
            self.head.value = value
        return True

    def insert_at_first(self, value):
        if self.head.next:
            new_elem = ListElem(self.head, value)
            self.head = new_elem
        else:
            self.head.value = value

        return self.head.value


    def delete(self, value):
        current = self.head.next

        if value and self.head.value and self.head.value == value:
            del self.head
            self.head = current
            self.reset()
            return True

        previous = self.head

        while current:
            if current.value == value:
                previous.next = current.next
                del current
                self.current = previous
                return True
            else:
                previous = current
                current = current.next

        return False

    def get_last(self):
        while self.current:
            self.current = self.current.next

        return self.current.value 

class Stack:
    def __init__(self):
        self.stack = List()
        self.last_inserted = None

    def push(self, value):
        self.stack.insert(value)
        self.last_inserted = value

    def pop(self):
        self.stack.delete(self.last_inserted)
        last = self.last_inserted
        self.last_inserted = self.stack.get_last()
	return last
