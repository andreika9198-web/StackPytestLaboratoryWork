import pytest
from Class.my_class import Queue,QueuePriority,User
#Тестируем класс Queue
@pytest.fixture()
def queue_obj():
    """
    Создал пустой стек
    """
    return Queue(10)

@pytest.fixture()
def queue_obj_full():
    """
    Создал полный стек
    """
    queue = Queue(10)
    for i in range(10):
        queue.enqueue(i)
    return queue

@pytest.fixture()
def queue_obj_filled():
    """
    Создал частично заполненный стек
    """
    queue = Queue(10)
    for i in range(5):
        queue.enqueue(i)
    return queue
#Тестируем класс QueuePriority
@pytest.fixture()
def queue_priority_obj():
    """
    Создал пустой стек
    """
    return QueuePriority(10)


@pytest.fixture()
def queue_priority_obj_filled_1():
    """
    Создал частично заполненный стек
    """
    queue = QueuePriority(10)
    for i in range(5):
        queue.enqueue({"priority": f'data_{i}'})
    for i in range(4):
        queue.enqueue({"no_priority": f'data_{i}'})
    return queue

@pytest.fixture()
def queue_priority_obj_filled_2():
    """
    Создал частично заполненный стек без приоритета
    """
    queue = QueuePriority(10)
    for i in range(4):
        queue.enqueue({"no_priority": f'data_{i}'})
    return queue

@pytest.fixture()
def queue_priority_obj_filled_3():
    """
    Создал частично заполненный стек приоритетными элементами
    """
    queue = QueuePriority(10)
    for i in range(5):
        queue.enqueue({"priority": f'data_{i}'})
    return queue

#Тестируем класс User
@pytest.fixture()
def user_obj():
    return User()

@pytest.fixture()
def user_obj_filled():
    user = User()
    user.add_user({"name": "Иван", "password": "123"})
    user.add_user({"name": "Макс", "password": "123"})
    user.add_user({"name": "Алекс", "password": "123"})
    return user