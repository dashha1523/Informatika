# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # разбиваем строки на списки участников
    list1 = group1.split(separator)
    list2 = group2.split(separator)
    return sorted(set(list1) & set(list2))  # находим пересечение множеств и возвращаем отсортированный список

# Проверка работы функции с разделителем "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|'
)
print("Общие участники:", common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
