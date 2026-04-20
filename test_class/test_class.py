import pytest

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
