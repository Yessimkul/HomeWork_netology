file_name = 'recepie.txt'


def recipe(file_name):
    with open(file_name, encoding='utf8') as f:
        global cook_book
        cook_book = {}
        for dish in f:
            dish_name = dish.strip()
            counter = int(f.readline().strip())
            ingredients = []
            for item in range(counter):
                name, qty, measure = f.readline().strip().split('|')
                ingredients.append({'name': name, 'quantity': qty, 'measure': measure})
            cook_book[dish_name] = ingredients
            f.readline()
        return cook_book


recipe(file_name)


def get_shop_list_by_dishes(dishes, person_count):

    shop_list = {}
    qty_1 = {}

    for k, v in cook_book.items():
        if k in dishes:
            for i in v:
                ing = i['name']
                quant = int(i['quantity']) * int(person_count)
                meas = i['measure']
                qty_1 = {'quntity': quant, 'measure': meas}
                shop_list.setdefault(ing,qty_1)
    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3))
