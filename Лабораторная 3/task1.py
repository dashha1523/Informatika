# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def f(items_list, target_item): #функция, принимающая 2 аргументы

    for i, item in enumerate(items_list): #равен ли элемент списка товару
        if item == target_item: #если да, возвращаем его индекс
            return i
    return None #если товар не найден

for find_item in ['банан', 'груша', 'персик']:
    index_item = f(items_list, find_item) #поиск индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

