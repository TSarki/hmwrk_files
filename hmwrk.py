from pprint import pprint
cook_book = {}
with open('recipes.txt', 'rt', encoding = 'utf-8') as file:
    for i in file:
        dish_name = i.strip()
        recipe = []
        ingredients_amount = file.readline()
        for m in range(int(ingredients_amount)):
            ingredient = file.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            recipe.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book[dish_name] = recipe

def get_shop_list_by_dishes(dishes, person_count):
    if person_count > 0:
        shop_list = {}
        ingredients = []
        for dish in dishes:
            dish_ing = cook_book[dish][0:]
            for item in dish_ing:
                ingredients.append(item)
        for ing in ingredients:
            feature = {"measure": ing["measure"], "quantity": int(int(ing["quantity"])*person_count)}  
            if ing['ingredient_name'] in shop_list.keys():
                shop_list[ing['ingredient_name']]['quantity'] += feature['quantity'] 
            else:
                shop_list[ing['ingredient_name']] = feature
        return shop_list
    else:
        return 'Недостаточное количество персон!'

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 0))