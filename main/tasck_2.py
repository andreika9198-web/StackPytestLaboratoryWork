from Class.my_class import QueuePriority
# IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ InsertWithPriority — добавление элемента c приоритетом в очередь.
# ■ -PullHighestPriorityElement - удаление элемента с самым высоким
# приоритетом из очереди.
# ■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание,
# что элемент не удаляется из очереди.
# ■ Show — отображение всех элементов очереди на экран.
# При показе элемента также необходимо отображать приоритет.

if __name__ == '__main__':
    queue_1 = QueuePriority(10)
    print('Печать')
    # list_queue = []
    while True:
        navigation = input(f"""
1.Проверка очереди на пустоту.
2.Проверка очереди на заполнение.
3.Добавление элемента в очередь.
4.Удаление элемента из очереди.
5.Отображение всех элементов очереди на экран.
6.Добавление элемента c приоритетом в очередь
7.Удаление элемента с самым высоким приоритетом из очереди.
0.Выход
Ваш вариант: """).strip()
        if navigation == '0':
            break
        elif navigation == '1':
            if queue_1.is_empty():
                print(f'Очередь для печати пуста')
            else:
                print(f'Есть очередь')
        elif navigation == '2':
            if queue_1.is_full():
                print(f'Нет свободной очереди для печати')
            else:
                print(f'Свободная  очередь есть')
        elif navigation == '3':
            my_data = input("Данные для печати: ")
            queue_1.enqueue({"no_priority": my_data})
        elif navigation == '4':
            if queue_1.dequeue():
                print('Номер был успешно удален')
            else:
                print("Список пуст")
        elif navigation == '5':
            queue_1.show()
        elif navigation == '6':
            my_data = input("Данные для печати в приоритет: ")
            if queue_1.insert_with_priority({"priority": my_data}):
                print("Данные успешно добавлены")
            else:
                print("Данные не были добавлены")
        elif navigation == '7':
            queue_1.pull_highest_priority_element()
        else:
            print("Такого варианта нету")