import os
from pprint import pprint
from tkinter import N
cook_book = {}
with open(r'recipes\recipes.txt', 'rt', encoding = 'utf-8') as file:
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

direction = r'C:\Users\user\Desktop\hmwrk_files'
dir_list = os.listdir(direction)
files_list = []
for i in dir_list:
    if '.txt' in i:
        files_list.append(i)
def file_combiner(filelist):
    line_amount_list = {}
    sorted_line_amount_list = {}
    for l in files_list:
        with open(l, 'rt', encoding = 'utf-8') as file:
            line_amount = len(file.readlines())
            line_amount_list[l] = line_amount
    sorted_line_amount_keys = sorted(line_amount_list, key=line_amount_list.get)  
    for s in sorted_line_amount_keys:
        sorted_line_amount_list[s] = line_amount_list[s]
    # return sorted_line_amount_list 
    with open(r'recipes\result.txt', 'w', encoding = 'utf-8') as document:
        for t in sorted_line_amount_list:
            document.write(f'{t}\n')
            document.write(f'{sorted_line_amount_list[t]}\n')
            with open(t, 'rt', encoding = 'utf-8') as file:
                content = file.read()
            document.write(f'{content}\n')
        return document   


print(file_combiner('files_list'))
