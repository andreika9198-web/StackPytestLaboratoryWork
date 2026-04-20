from Class.my_class import Node,Queue
# IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ Enqueue — добавление элемента в очередь.
# ■ Dequeue — удаление элемента из очереди.
# ■ Show — отображение всех элементов очереди на
# экран.
if __name__ == '__main__':
    queue_1 = Queue(10)
    print('Запись на очередь')
    list_queue = []
    while True:
        navigation = input(f"""
        1.Проверка очереди на пустоту.
        2.Проверка очереди на заполнение.
        3.Добавление элемента в очередь.
        4.Удаление элемента из очереди.
        5.отображение всех элементов очереди на экран.
        0.Выход
        Ваш вариант: """).strip()
        if navigation == '0':
            break
        elif navigation == '1':
            if queue_1.is_empty():
                print(f'Все места свободные')
            else:
                print(f'Есть очередь')
        elif navigation == '2':
            if queue_1.is_full():
                print(f'Нет свободных мест')
            else:
                print(f'Свободные места есть')
        elif navigation == '3':
            try:
             my_number = int(input("Введите номер для добавление очередь: "))
            except ValueError:
                print("Введите целое число")
            else:
                if not my_number in list_queue:
                    list_queue.append(my_number)
                    queue_1.enqueue(my_number)
                    print('Номер был успешно добавлен')
                else:
                    print("Такой номер уже есть")
        elif navigation == '4':

            list_queue.remove(queue_1.dequeue())
            print('Номер был успешно удален')
            print(list_queue)
        elif navigation == '5':
            queue_1.show()

        else:
            print("Такого варианта нету")