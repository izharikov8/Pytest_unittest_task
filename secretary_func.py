documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def get_name(data):
    doc_num = input("Введите номер документа: ")
    for el in data:
        if doc_num == el["number"]:
            return el["name"]
    else:
        print("Такого документа нет в директории.")


def get_shelf(data):
    doc_num = input("Введите номер документа: ")
    for el in data.items():
        if doc_num in el[1]:
            return f"Номер полки - {el[0]}."
    else:
        return f"Документа с номером {doc_num} нет в директории."


def get_list(data):
    for el in data:
        doc_type = el["type"]
        doc_num = el["number"]
        name = el["name"]
        return f'{doc_type} "{doc_num}" "{name}"'


def add_doc(data, data_2):
    shelf_num = input("Введите на какую полку добавить документ: ")
    doc_num = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    doc_owner = input("Введите владельца документа: ")
    if shelf_num in data_2.keys():
        data_2[shelf_num].append(doc_num)
        new_add = {"type": doc_type, "number": doc_num, "name": doc_owner}
        data.append(new_add)
    return "Yes, doc added."
    # else:
    #     print("Такой полки не существует, введите существующую полку из: ", list(data_2.keys()))


def delete_doc(data, data_2):
    number = input('Введите номер удаляемого документа: ')
    for doc in data:
        if doc['number'] == number:
            data.remove(doc)
    for shelf in data_2:
        if number in data_2[shelf]:
            data_2[shelf].remove(number)
            return f'Документ {number} удалён.'


def move_doc(data):
    shelf_num = input("Введите номер полки для переноса: ")
    doc_num = input("Введите номер документа для переноса: ")
    if shelf_num in data.keys():
        for key, value in data.items():
            if doc_num in value:
                value.remove(doc_num)
                data[shelf_num].append(doc_num)
    return 'Документ успешно перенесен на полку.'
    #         break
    #     else:
    #         return print("Такого документа нет.")
    # else:
    #     return print("Такой полки нет.")


def add_shelf(data):
    to_add = input("Введите номер полки для создания: ")
    if to_add in data.keys():
        print("Полка уже существует.")
    else:
        data.update({to_add: []})
        return f'Полка {to_add} добавлена.'