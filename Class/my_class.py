class Node:
    def __init__(self,data , next_node = None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self,max_length, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.max_length = max_length

    def enqueue(self, data):
        if self.is_full():
            print('Очередь переполнена')
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
            return dequeue_item.data

    def size_stack(self):
        counter = 0
        stack_item = self.head
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def peek_first(self):
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.head.data)

    def peek_last(self):
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.tail.data)

    def show(self):
        if not self.head:
            print(f'Очередь пуста')
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next_node

    def is_full(self):
        if self.size_stack() == self.max_length:
            # print('Стек полон')
            return True
        else:
            # print('Стек пуст')
            return False

    def is_empty(self):
        if not self.head:
            #Очередь пуста
            return True
        else:
            # Очередь не пустая
            return False

if __name__ == '__main__':
    node = Node(1)
    queue = Queue(3, node, node)
    for i in range(2, 6):
        queue.enqueue(i)
    queue.show()

    print(queue.is_full())
    print(queue.is_empty())
    for _ in range(queue.size_stack()):
        queue.dequeue()
    print(queue.is_empty())
