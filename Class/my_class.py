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
            return False

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        return True

    def dequeue(self):
        """
        Метод для удаления данных из очереди
        :return:
            None или dequeue_item.data(удаленные данные)
        """
        if not self.head:
            return False
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
            Возвращает строку очередь пуста или первый элемент
        """
        if not self.head:
            print(f'Очередь пуста')
            return False
        else:
            print(self.head.data)
            return True

    def peek_last(self):
        """
        Метод для отображения последнего элемента
        :return:
            Возвращает строку очередь пуста или последний элемент
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
        :param data:

        """
        if not isinstance(data, dict) or "priority" not in data:
            print('Ошибка: добавить можно только словарь с ключом "priority"')
            return None
        if self.size() >= self.max_length:
            print("Очередь переполнена")
            return None

        new_node = Node(data)
        if not self.head:
            # Очередь пуста
            self.head = new_node
            self.tail = new_node
            return True
        elif "priority" not in self.head.data:
            # Голова НЕ приоритетная → вставляем в начало
            new_node.next_node = self.head
            self.head = new_node
            return True
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
            return True
    def pull_highest_priority_element(self):
        """
        Удаляет самый приоритетный элемент (голову)
        :return: удаленный элемент или None
        """
        if not self.head:
            print("Очередь пуста")
            return None

        if not isinstance(self.head.data, dict) or "priority" not in self.head.data:
            print("Нет приоритетных элементов")
            return None

        # Удаляем голову (она приоритетная)
        dequeue_item = self.head
        self.head = self.head.next_node
        if not self.head:  # очередь стала пустой
            self.tail = None

        return dequeue_item.data

    def peek(self):
        """
        Просмотр первого элемента (если он приоритетный)
        :return
            возвращает None или self.head.data(первый приоритетный элемент)
        """
        if not self.head:
            print("Очередь пуста")
            return None

        if isinstance(self.head.data, dict) and "priority" in self.head.data:
            return self.head.data
        else:
            return None

    def show(self):
        """
        Метод для отображения все элементов очереди.
        Отображает сначала приоритетные элементы и дает им порядковый номер,
        потом идет отображение не приоритетных элементов с присвоением номера
        """
        if not self.head:
            print(f'Очередь пуста')
        else:
            current = self.head
            count = 0
            while current:
                if isinstance(current.data, dict) and "priority" in current.data:
                    count += 1
                    print(f'Приоритетный элемент номер {count} данные элемента - {current.data["priority"]}')
                elif isinstance(current.data, dict) and "no_priority" in current.data:
                    count += 1
                    print(f'Не приоритетный элемент номер {count} данные элемента - {current.data["no_priority"]}')
                else:
                    count += 1
                    print(current.data)
                current = current.next_node

    def enqueue(self, data):
        """
        Метод для добавления данных в очередь
        :param data:
            принимает любые данные
        :return:
        """
        if self.size() >= self.max_length - 2:
            #Зарезервировал два элемента для приоритетных
            print('Очередь переполнена')
            return

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

class User:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_user(self,data):
        """
        Метод для добавления новых пользователей
        :param data:
            Данные нового пользователя
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_user(self, rm_data):
        """
        Метод для удаления пользователя.
        :param rm_data:
            Имя пользователя для удаления (строка)
        :return:
            данные удалённого пользователя или None
        """
        if not self.head:
            print(f'Список пуст')
            return None
        if rm_data == self.head.data['name']:
            removed_node = self.head
            self.head = self.head.next_node
            print(f"Удалили пользователя {removed_node.data['name']}")
            return removed_node.data

        current_node = self.head
        while current_node and current_node.next_node:
            if current_node.next_node.data['name'] == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                return removed_node.data
            current_node = current_node.next_node
        return None

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

    def update_field(self,data,new_data,search):
        """
        Универсальный метод для изменения любого поля пользователя

         param data:
            data: имя пользователя для поиска
            new_data: новое значение
            search: поле для изменения ('name', 'password')
        return:
            True если данные успешно изменены,
            False если очередь пуста или пользователь не найден
        """

        if not self.head:
            print(f'Очередь пуста')
            return False
        else:
            current = self.head
            while current:
                if current.data['name'] == data:
                    old_data = current.data[search]
                    current.data[search] = new_data
                    print(f"Данные {search}: {old_data} были изменены на {new_data}")
                    return True
                current = current.next_node
            print("Пользователь не найден")
            return False

    def is_user(self,data):
        """
        Метод для проверки существования пользователя в очереди.
        :param data:
            Имя пользователя для поиска (строка)
        :return:
         True если пользователь найден, False если нет
        """
        if not self.head:
            print(f'Очередь пуста')
            return False
        else:
            current = self.head
            while current:
                if current.data['name'] == data:
                    print(f"Пользователь {data} был найден")
                    return True
                current = current.next_node
            print(f"Пользователь {data} не был найден")
            return False
# if __name__ == '__main__':
#
#     node = Node({"name": "Иван", "password": "123"})
#     user = User(node, node)
#     user.add_user({"name": "Макс", "password": "123"})
#     user.add_user({"name": "Алекс", "password": "123"})
#     user.add_user({"name": "Иван", "password": "123"})
#     user.show()
#     print('_____')
#     user.remove_user("Иван")
#     user.show()
#     print('_____')
#     user.update_field( "Алекс","Андрей","name")
#     user.show()
#     print('_____')
#     user.update_field("Макс", '345',"password")
#     user.show()
#     user.is_user("Макс")
#     user.is_user("Антон")

    # print('_____')
    # user.rename({"name": "Алекс", "password": "123"},"Андрей")
    # user.show()
    # print('_____')
    # user.new_password({"name": "Макс", "password": "123"},'345')
    # user.show()
#     queue = Queue(3, node, node)
#     for i in range(2, 6):
#         queue.enqueue(i)
#     queue.show()
#
#     print(queue.is_full())
#     print(queue.is_empty())
#     for _ in range(queue.size()):
#         queue.dequeue()
#     print(queue.is_empty())
#
# d1 = {"name": "Иван"}
# d2 = {"priority": "1"}
# d3 = {"priority": "3"}
# node = Node(d1)
# queue_1 = QueuePriority(10, node, node)
# for i in range(3):
#     queue_1.enqueue(i)
# queue_1.show()
# print('____')
# queue_1.insert_with_priority({"priority": "1"})
# queue_1.insert_with_priority(d3)
# queue_1.enqueue({"no_priority": "5"})
# queue_1.enqueue(10)
# queue_1.show()
# print('____')
# queue_1.pull_highest_priority_element()
# queue_1.show()
# print('____')
# queue_1.pull_highest_priority_element()
# queue_1.show()
# print('____')
# queue_1.pull_highest_priority_element()
# queue_1.show()
# print('____')
# queue_1.insert_with_priority({"no_priority": "7"})
# queue_1.show()
#
# print('____')
# queue_1.insert_with_priority({"priority": "6"})
# queue_1.show()

