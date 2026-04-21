import pytest

#Тестируем класс Queue
def test_01_01_enqueue(queue_obj_full):
    """
    Тест для проверки добавление в полный стек
    """
    assert queue_obj_full.enqueue(11) == False

def test_01_02_enqueue(queue_obj):
    """
    Тест для проверки добавление в пустой стек
    """
    assert queue_obj.enqueue(11) == True
    assert queue_obj.head.data == 11

def test_01_03_enqueue(queue_obj_filled):
    """
    Тест для проверки добавление в не пустой стек
    """
    assert queue_obj_filled.enqueue(5) == True
    assert queue_obj_filled.head.data == 0

def test_02_01_dequeue(queue_obj):
    """
    Тест для проверки удаления данных из пустого стека
    """
    assert queue_obj.dequeue() == False

def test_02_02_dequeue(queue_obj_filled):
    """
    Тест для проверки удаления данных из стека
    """
    assert queue_obj_filled.dequeue() == 0

def test_03_01_size(queue_obj_filled):
    """
    Тест для проверки подсчета количества элементов в стеке
    """
    assert  queue_obj_filled.size() == 5

def test_04_01_peek_first(queue_obj):
    """
    Тест для проверки отображения первого элемента из пустого стека
    """
    assert queue_obj.peek_first() == False

def test_04_02_peek_first(queue_obj_filled):
    """
    Тест для проверки отображения первого элемента из пустого стека
    """
    assert queue_obj_filled.peek_first() == True
    assert queue_obj_filled.head.data == 0

def test_05_01_peek_last(queue_obj):
    """
    Тест для проверки отображения последнего элемента из пустого стека
    """
    assert queue_obj.peek_last() == False

def test_05_02_peek_last(queue_obj_filled):
    """
    Тест для проверки отображения последнего элемента из стека
    """
    assert queue_obj_filled.peek_last() == True
    assert queue_obj_filled.tail.data == 4

def test_06_01_show(queue_obj):
    """
    Тест для проверки отображения всех элементов из пустого стека
    """
    assert queue_obj.show() == False

def test_06_02_show(queue_obj_filled):
    """
    Тест для проверки отображения всех элементов из стека
    """
    assert queue_obj_filled.show() == True

def test_07_01_is_full(queue_obj_full):
    """
    Тест для проверки является ли очередь полностью заполненной(стек полон)
    """
    assert queue_obj_full.is_full() == True

def test_07_02_is_full(queue_obj_filled):
    """
    Тест для проверки является ли очередь полностью заполненной
    (стек частично заполнен)
    """
    assert queue_obj_filled.is_full() == False

def test_08_01_is_empty(queue_obj):
    """
    Тест для проверки является ли очередь полностью пустой
    (стек пуст)
    """
    assert queue_obj.is_empty() == True

def test_08_02_is_empty(queue_obj_filled):
    """
    Тест для проверки является ли очередь полностью пустой
    (стек частично заполнен)
    """
    assert queue_obj_filled.is_empty() == False

#Тестируем класс QueuePriority
def test_09_01_insert_with_priority(queue_priority_obj):
    """
    Тест для проверки добавление в пустой стек
    """
    assert queue_priority_obj.insert_with_priority(1) == False
    assert queue_priority_obj.insert_with_priority({"no_priority": f'data_7'}) == False
    assert queue_priority_obj.insert_with_priority({"priority": f'data_7'}) == True
    assert queue_priority_obj.head.data == {"priority": f'data_7'}

def  test_09_02_insert_with_priority(queue_priority_obj_filled_2):
    """
    Тест для проверки добавление в частично заполненный стек,
    не приоритетными элементами
    """
    assert queue_priority_obj_filled_2.insert_with_priority({"priority": f'data_7'}) == True
    assert queue_priority_obj_filled_2.head.data == {"priority": f'data_7'}

def test_09_03_insert_with_priority(queue_priority_obj_filled_1):
    """
    Тест для проверки добавление в частично заполненный стек,
    приоритетными и не приоритетными элементами
    """
    assert queue_priority_obj_filled_1.insert_with_priority({"priority": f'data_7'}) == True
    assert queue_priority_obj_filled_1.head.data != {"priority": f'data_7'}
    assert queue_priority_obj_filled_1.tail.data != {"priority": f'data_7'}

def test_09_04_insert_with_priority(queue_priority_obj_filled_3):
    """
    Тест для проверки добавление в частично заполненный стек,
    приоритетными элементами
    """
    assert queue_priority_obj_filled_3.insert_with_priority({"priority": f'data_7'}) == True
    assert queue_priority_obj_filled_3.tail.data == {"priority": f'data_7'}

def test_10_01_pull_highest_priority_element(queue_priority_obj):
    """
    Тест для проверки удаления из пустого стека стек,
    """
    assert queue_priority_obj.pull_highest_priority_element() == False
    queue_priority_obj.insert_with_priority({"priority": f'data_7'})
    assert queue_priority_obj.pull_highest_priority_element() == {"priority": f'data_7'}
    assert queue_priority_obj.tail is None

def test_10_02_pull_highest_priority_element(queue_priority_obj_filled_2):
    """
    Тест для проверки удаления из частично заполненного стека,
    не приоритетными элементами
    """
    assert queue_priority_obj_filled_2.pull_highest_priority_element() == False

def test_11_01_peek(queue_priority_obj):
    """
    Тест для проверки возращения первого приоритетного элемента(стек пуст)
    """
    assert queue_priority_obj.peek() == False

def test_11_02_peek(queue_priority_obj_filled_1):
    """
    Тест для проверки возращения первого приоритетного
    элемента(частично заполненного стека)
    """
    assert queue_priority_obj_filled_1.peek() == {'priority': 'data_0'}

def test_11_03_peek(queue_priority_obj_filled_2):
    """
    Тест для проверки возращения первого приоритетного
    элемента(частично заполненного стека не приоритетными элементами)
    """
    assert queue_priority_obj_filled_2.peek() == False

def test_12_01_show(queue_priority_obj):
    """
    Тест для проверки отображения всех элементов очереди.(пустой стек)
    """
    assert queue_priority_obj.show() == False

def test_12_02_show(queue_priority_obj_filled_1):
    """
    Тест для проверки отображения всех элементов очереди.
    (частично заполненного стека)
    """
    assert queue_priority_obj_filled_1.show() == True

def test_13_01_enqueue(queue_priority_obj_filled_1):
    """
    Тест для проверки добавление в не полный стек, свободное место 1,
     но зарезервированного для приоритета
    """
    assert queue_priority_obj_filled_1.enqueue({"no_priority": f'data_7'}) == False

def  test_13_02_enqueue(queue_priority_obj):
    """
    Тест для проверки удаления данных из пустого стека
    """
    assert queue_priority_obj.enqueue({"no_priority": f'data_7'}) == True
    assert queue_priority_obj.head.data == {"no_priority": f'data_7'}

def test_13_03_enqueue(queue_priority_obj_filled_2):
    """
    Тест для проверки удаления данных из стека
    """
    assert queue_priority_obj_filled_2.enqueue({"no_priority": f'data_7'}) == True
    assert queue_priority_obj_filled_2.tail.data == {"no_priority": f'data_7'}

#Тестируем класс User
def test_14_01_add_user(user_obj):
    """
    Тест для проверки добавление в данных стек
    """
    user_obj.add_user({"name": "Иван", "password": "123"})
    assert user_obj.head.data == {"name": "Иван", "password": "123"}
    user_obj.add_user({"name": "Макс", "password": "123"})
    assert user_obj.tail.data == {"name": "Макс", "password": "123"}

def test_15_01_remove_user(user_obj):
    """
    Тест для проверки удаления данных из пустого стека
    """
    assert user_obj.remove_user('Макс') == False

def test_15_02_remove_user(user_obj):
    """
    Тест для проверки удаления данных из головы стека
    """
    user_obj.add_user({"name": "Иван", "password": "123"})
    assert user_obj.remove_user("Иван") == {"name": "Иван", "password": "123"}

def test_15_03_remove_user(user_obj_filled):
    """
    Тест для проверки удаления данных из хвоста стека и проверка на
    отсутствие удаляемых данных
    """
    assert user_obj_filled.remove_user("Алекс") == ({"name": "Алекс", "password": "123"})
    assert user_obj_filled.tail.data == {"name": "Макс", "password": "123"}
    assert user_obj_filled.remove_user("Антон") == False

def test_16_01_show(user_obj):
    """
    Тест для проверки отображения всех элементов из пустого стека
    """
    assert user_obj.show() == False

def test_16_02_show(user_obj_filled):
    """
    Тест для проверки отображения всех элементов из стека
    """
    assert user_obj_filled.show() == True

def test_17_01_update_field(user_obj):
    """
    Тест для проверки изменения имени из пустого стека
    """
    assert user_obj.update_field("Алекс","Антон","name") == False
    assert user_obj.update_field("Алекс", "456", "password") == False

def test_17_02_update_field(user_obj_filled):
    """
    Тест для проверки изменения имени и пароля
    """
    assert user_obj_filled.update_field("Алекс","Антон","name") == True
    assert user_obj_filled.update_field("Алекс", "Антон", "name") == False
    assert user_obj_filled.update_field("Антон", "456", "password") == True

