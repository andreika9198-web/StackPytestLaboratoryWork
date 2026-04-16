class Node:
    """
    Узел односвязного списка для использования в стеке
    data:
        Хранимые данные
    next_node:
        Ссылка на следующий узел
    """
    def __init__(self,data , next_node = None):
        self.data = data
        self.next_node = next_node

class Queue:
    """
    Класс для создания очереди
    Помимо стандартных методов enqueue и dequeue
    Используются: is_empty, is_full, size_stack,peek_first,peek_last,show,
    """
    def __init__(self,max_length, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.max_length = max_length

    def enqueue(self, data):
        """
        Метод для добавления данных в очередь
        :param data:
            принимает любые данные
        :return:
        """
        if self.size() >= self.max_length:
            print('Очередь переполнена')
            return

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления данных из очереди
        :return:
            None или dequeue_item.data(удаленные данные)
        """
        if not self.head:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
            return dequeue_item.data

    def size(self):
        """
        Метод для подсчета количество элементов в очереди
        :return:
            counter
        """
        counter = 0
        stack_item = self.head
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def peek_first(self):
        """
        Метод для отображения первого элемента
        :return:
            Возращает строку очередь пуста или первый элемент
        """
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.head.data)

    def peek_last(self):
        """
        Метод для отображения последнего элемента
        :return:
            Возращает строку очередь пуста или последний элемент
        """
        if not self.head:
            print(f'Очередь пуста')
        else:
            print(self.tail.data)

    def show(self):
        """
        Метод для отображения все элементов очереди
        """
        if not self.head:
            print(f'Очередь пуста')
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next_node

    def is_full(self):
        """
           Метод для определения является ли очередь полностью заполненным
        :return:
            True или False
        """
        if self.size() == self.max_length:
            return True
        else:
            return False

    def is_empty(self):
        """
           Метод для определения является ли очередь полностью пустой
        :return:
            True или False
        """
        if not self.head:
            #Очередь пуста
            return True
        else:
            # Очередь не пустая
            return False

class QueuePriority(Queue):
    def __init__(self, max_length, head=None, tail=None):
        super().__init__(max_length, head, tail)

    def insert_with_priority(self, data):
        """
        Вставка элемента с приоритетом
        Приоритетные элементы вставляются ПОСЛЕ всех существующих приоритетных
        """
        if self.size() >= self.max_length:
            print("Очередь переполнена")
            return

        new_node = Node(data)

        if not self.head:
            # Очередь пуста
            self.head = new_node
            self.tail = new_node

        elif "priority" not in self.head.data:
            # Голова НЕ приоритетная → вставляем в начало
            new_node.next_node = self.head
            self.head = new_node

        else:
            # Ищем последний приоритетный элемент
            current = self.head
            while current.next_node and "priority" in current.next_node.data:
                current = current.next_node

            # Вставляем после последнего приоритетного
            new_node.next_node = current.next_node
            current.next_node = new_node

            # Если вставили в конец, обновляем tail
            if not new_node.next_node:
                self.tail = new_node


def pull_highest_priority_element(self):
    """Удаляет самый приоритетный элемент (голову)"""
    if not self.head:
        return None

    # Проверяем, что голова - приоритетная
    if isinstance(self.head.data, dict) and "priority" in self.head.data:
        dequeue_item = self.head
        self.head = self.head.next_node
        if not self.head:  # очередь стала пустой
            self.tail = None
        return dequeue_item.data
    else:
        print("Нет приоритетных элементов")
        return None

if __name__ == '__main__':
    node = Node(1)
    queue = Queue(3, node, node)
    for i in range(2, 6):
        queue.enqueue(i)
    queue.show()

    print(queue.is_full())
    print(queue.is_empty())
    for _ in range(queue.size()):
        queue.dequeue()
    print(queue.is_empty())

d1 = {"name": "Иван"}
d2 = {"priority": "1"}
d3 = {"priority": "3"}
node = Node(d1)
queue_1 = QueuePriority(7, node, node)
for i in range(3):
    queue_1.enqueue(i)
queue_1.show()
print('____')
queue_1.insert_with_priority(d2)
queue_1.insert_with_priority(d3)
queue_1.show()

