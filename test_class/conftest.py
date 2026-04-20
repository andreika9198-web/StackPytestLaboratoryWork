import pytest
from Class.my_class import Queue,QueuePriority,User

@pytest.fixture()
def queue_obj():
    return Queue(10)

@pytest.fixture()
def queue_obj_full():
    queue = Queue(10)
    for i in range(10):
        queue.enqueue(i)
    return queue

@pytest.fixture()
def queue_obj_filled():
    queue = Queue(10)
    for i in range(5):
        queue.enqueue(i)
    return queue