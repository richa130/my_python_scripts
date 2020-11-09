"""
***************************************************************************
Filename:      lab_7

Author:        Richa Bavadekar

Date:          11/25/19

Modifications: Richa Bavadekar - 11/25/19

Description:   This lab updates lab 5 using dictionaries and lists to make the process more efficient.
***************************************************************************
"""

#3 dictionaries for the 3 recipes
chocolate_recipe = {'Flour':0.158, 'Sugar':0.245, 'Unsweetened Cocoa Powder':0.056, 'Baking Powder':0.004, 'Baking Soda':0.006,
                    'Salt':0.004, 'Egg':0.090, 'Buttermilk':0.18, 'Canola Oil':0.081, 'Vanilla Extract':0.006, 'Boiling Water':0.17}
red_velvet_recipe = {'Flour':0.224, 'Sugar':0.224, 'Baking Soda':0.007, 'Salt':0.004, 'Unsweetened Cocoa Powder':0.004,
                     'Canola Oil':0.24, 'Buttermilk':0.179, 'Egg':0.09, 'Red Food Coloring':0.021, 'Vanilla Extract':0.003,
                     'Distilled Vinegar':0.004}
lemon_recipe = {'Butter':0.085, 'Sugar':0.15, 'Egg':0.09, 'Sifted Self-Rising Flour':0.156, 'Buttermilk':0.09, 'Vanilla Extract':0.002,
                'Egg Yolk Filling':0.179, 'Sugar Filling':0.113, 'Butter Filling':0.021, 'Lemon Juice and Zest Filling':0.114}

"""
***************************************************************************
Function:   calc_ingredient(weight, recipe)

Parameters: weight - total weight of all the sizes ordered
            recipe - dictionary of specific recipe to be used

Outputs: None 

Returns: List of specific ingeredient weights

Author:  Richa Bavadekar 

Date:  11/25/19

Modifications: 11/25/19

Description:
This function returns a list that contains the specific ingredient weights.
The first parameter is a number. The second parameter is a dictionary.
***************************************************************************
"""
def calc_ingredient(weight, recipe):
    ingredient_list = []
    for key, value in recipe.items():
        ingredient = round(weight*value, 1)
        ingredient_list.append(ingredient)
    return ingredient_list

"""
***************************************************************************
Function:   print_ingredients(ingredient_list, names_list)

Parameters: ingredient_list - List of specific ingeredient weights
            names_list - List of specific ingeredient names

Outputs: The ingredient name and its corresponding weight

Returns: None

Author:  Richa Bavadekar 

Date:  11/25/19

Modifications: 11/25/19

Description:
This function prints out the ingredient name and its corresponding weight.
The first  and second parameters are lists.
***************************************************************************
"""
def print_ingredients(ingredient_list, names_list):
    for(ingredient, name) in zip(ingredient_list, names_list):
        print(name,":",ingredient,"Oz")


cake_type = input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: ")
chocolate_weight = 0
chocolate_type_regular = 0
chocolate_type_large = 0
red_velvet_weight = 0
red_velvet_type_regular = 0
red_velvet_type_large = 0
lemon_weight = 0
lemon_type_regular = 0
lemon_type_large = 0
while not(cake_type == 'q' or cake_type == 'Q'):
    cake_size = input("Please select cake size; Enter L for large, R for regular: ")

    if cake_type == "1":
        if cake_size == "R":
            chocolate_type_regular += 1
            chocolate_weight += 64
        else:
            chocolate_type_large += 1
            chocolate_weight += 112

    if cake_type == '2':
        if cake_size == 'R':
            red_velvet_type_regular += 1
            red_velvet_weight += 64
        else:
            red_velvet_type_large += 1
            red_velvet_weight += 112

    if cake_type == '3':
        if cake_size == 'R':
            lemon_type_regular += 1
            lemon_weight += 64
        else:
            lemon_type_large += 1
            lemon_weight += 112

    cake_type = input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: ")

if not(chocolate_type_regular + chocolate_type_large == 0):
    print("Ingredient Quantities for ", chocolate_type_large," Large and ", chocolate_type_regular  ," Regular Chocolate Cake\n")
    ingredient_list = calc_ingredient(chocolate_weight, chocolate_recipe)
    print_ingredients(ingredient_list, chocolate_recipe.keys())
    print("\nTotal:",float(chocolate_weight))

if not(red_velvet_type_large + red_velvet_type_regular == 0):
    print("Ingredient Quantities for ", red_velvet_type_large," Large and ", red_velvet_type_regular  ," Regular Red Velvet Cake\n")
    ingredient_list = calc_ingredient(red_velvet_weight, red_velvet_recipe)
    print_ingredients(ingredient_list, red_velvet_recipe.keys())
    print("\nTotal:",red_velvet_weight)

if not(lemon_type_large + lemon_type_regular == 0):
    print("Ingredient Quantities for ", lemon_type_large," Large and ", lemon_type_regular  ," Regular Lemon Cake\n")
    ingredient_list = calc_ingredient(lemon_weight, lemon_recipe)
    print_ingredients(ingredient_list, lemon_recipe.keys())
    print("\nTotal:",lemon_weight)

"""
Recording of the Output:
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 2
Please select cake size; Enter L for large, R for regular: R
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: L
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: R
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: L
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: R
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: L
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 2
Please select cake size; Enter L for large, R for regular: L
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: Q
Ingredient Quantities for  1  Large and  1  Regular Chocolate Cake

Flour : 27.8 Oz
Sugar : 43.1 Oz
Unsweetened Cocoa Powder : 9.9 Oz
Baking Powder : 0.7 Oz
Baking Soda : 1.1 Oz
Salt : 0.7 Oz
Egg : 15.8 Oz
Buttermilk : 31.7 Oz
Canola Oil : 14.3 Oz
Vanilla Extract : 1.1 Oz
Boiling Water : 29.9 Oz

Total: 176.0
Ingredient Quantities for  1  Large and  1  Regular Red Velvet Cake

Flour : 39.4 Oz
Sugar : 39.4 Oz
Baking Soda : 1.2 Oz
Salt : 0.7 Oz
Unsweetened Cocoa Powder : 0.7 Oz
Canola Oil : 42.2 Oz
Buttermilk : 31.5 Oz
Egg : 15.8 Oz
Red Food Coloring : 3.7 Oz
Vanilla Extract : 0.5 Oz
Distilled Vinegar : 0.7 Oz

Total: 176
Ingredient Quantities for  2  Large and  1  Regular Lemon Cake

Butter : 24.5 Oz
Sugar : 43.2 Oz
Egg : 25.9 Oz
Sifted Self-Rising Flour : 44.9 Oz
Buttermilk : 25.9 Oz
Vanilla Extract : 0.6 Oz
Egg Yolk Filling : 51.6 Oz
Sugar Filling : 32.5 Oz
Butter Filling : 6.0 Oz
Lemon Juice and Zest Filling : 32.8 Oz

Total: 288

Process finished with exit code 0
"""
