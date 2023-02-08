import os
from operator import itemgetter

with open('recipes.txt', 'rt', encoding='utf-8') as rec:
    cook_book = {}
    for line in rec:
        name_dish = line.strip()
        number_product = int(rec.readline())
        product = []
        for _ in range(number_product):
            pro = rec.readline().strip().split(' | ')
            ingredient_name, quantity, measure = pro
            product.append({'ingredient_name': ingredient_name, 
                            'quantity': quantity, 
                            'measure': measure})
        rec.readline()
        cook_book[name_dish] = product
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count: int):
    ingredient_for_dishes = {}
    for d in dishes:
        if d in cook_book:
            for pro in cook_book[d]:
                if not pro['ingredient_name'] in ingredient_for_dishes:
                    ingredient_for_dishes[pro['ingredient_name']] = {'measure': pro['measure'],
                                                       'quantity': (int(pro['quantity']) * person_count)}
                else:
                    ingredient_for_dishes['quantity'] += int(pro['quantity']) * person_count
        else:
            print('Нет такого блюда') 
    print(ingredient_for_dishes)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def reading_file(path_main):
    files = []
    for filename in list(os.listdir(path_main)):
        dic = {}
        with open(os.path.join("sorted", filename), 'r', encoding="utf8") as f:
            dic['Имя файла'] = filename
            lines = f.readlines()
            dic['Количество строк'] = len(lines)
            dic['Содержимое файла'] = lines
            files.append(dic)
    files.sort(key=itemgetter('Количество строк'))
    for item in files:
        print(f"{item['Имя файла']}\n{item['Количество строк']}\n{''.join(item['Содержимое файла'])}")
reading_file("sorted")
