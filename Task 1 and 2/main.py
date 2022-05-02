file_name = 'recepie.txt'


def recipe(file_name):
    with open(file_name, encoding='utf8') as f:
        cook_book = {}
        for dish in f:
            dish_name = dish.strip()
            counter = int(f.readline().strip())
            ingredients = []
            for item in range(counter):
                name, qty, measure = f.readline().strip().split('|')
                ingredients.append({'name': name, 'quantity': qty, 'measure': measure})
            cook_book[dish_name] = [ingredients]
            f.readline()
        print(cook_book)


# recipe(file_name)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }
    shop_list = {}
    qty = {}
    for k, v in cook_book.items():
        for dish in dishes:
            if dish in k:
                for i in v:
                    b = list(i.values())[0]
                    qty['measure'] = list(i.values())[2]
                    qty['quantity'] = (list(i.values())[1] * person_count)
                    shop_list = {b: qty}
                    print(shop_list)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
