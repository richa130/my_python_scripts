"""
***************************************************************************
Filename:      lab_5.py

Author:        Richa Bavadekar

Date:          11/19/19

Modifications: Richa Bavadekar - 11/19/19

Description:   This lab takes in user input for type of cake and size of cake, and prints out the ounces of each
               ingredient accordingly.
***************************************************************************
"""

# chocolate cake ingredient percentages divided by 100
cflour = 0.158
csugar = 0.245
ccocoa = 0.056
cbaking_powder = 0.004
cbaking_soda = 0.006
csalt = 0.004
cegg = 0.090
cbutter_milk = 0.18
ccanola_oil = 0.081
cvanilla_extract = 0.006
cboiling_water = 0.17


# red velvet cake ingredient percentages divided by 100
rflour = 0.224
rsugar = 0.224
rbaking_soda = 0.007
rsalt = 0.004
rcocoa_powder = 0.004
rcanola_oil = 0.24
rbuttermilk = 0.179
regg = 0.09
rfood_coloring = 0.021
rvanilla_extract = 0.003
rdistilled_vinegar = 0.004

# lemon cake percentages divided by 100
lbutter = 0.085
lsugar = 0.15
legg = 0.09
lflour = 0.156
lbuttermilk = 0.09
lvanilla_extract = 0.002
legg_yolk_filling = 0.179
lsugar_filling = 0.113
lbutter_filling = 0.021
llemon_juice_zest_filling = 0.114

"""
***************************************************************************
Function:   recipe(size, type)

Parameters: size - string R or L to determine the size 
            type - number 1, 2, or 3 to determine cake type 

Outputs: string with each ingredient and how much of it in ounces to use for this specific cake recipe 

Returns: None

Author:  Richa Bavadekar 

Date:  11/19/19

Modifications: 11/19/19

Description:
This function prints a string with a the amount of each ingredient in ounces needed for this specific cake recipe and 
size.
The first parameter is a string literal or variable.
The second parameter is a number. 
***************************************************************************
"""
def recipe(size, type):
    if size == "R":
        ounces = 64
        if type == 1:
            flour = round(ounces * cflour, 1)
            sugar = round(ounces * csugar, 1)
            cocoa = round(ounces * ccocoa, 1)
            baking_powder = round(ounces * cbaking_powder, 1)
            baking_soda = round(ounces * cbaking_soda, 1)
            salt = round(ounces * csalt, 1)
            egg = round(ounces * cegg, 1)
            butter_milk = round(ounces * cbutter_milk, 1)
            canola_oil = round(ounces * ccanola_oil, 1)
            vanilla_extract = round(ounces * cvanilla_extract, 1)
            boiling_water = round(ounces * cboiling_water, 1)
            print("Regular Chocolate Ingredient List:\nFlour:",flour, "Oz\nSugar:",sugar,"Oz\nCocoa Powder:",cocoa,
                  "Oz\nBaking Powder:",baking_powder,"Oz\nBaking Soda:",baking_soda,"Oz\nSalt:",salt,"Oz\nEgg:",egg,"Oz"
                  "\nButtermilk:",butter_milk,"Oz\nCanola Oil:",canola_oil,"Oz\nVanilla Extract:",vanilla_extract,
                  "Oz\nBoiling Water:",boiling_water,"Oz")
        if type == 2:
            flour = round(ounces * rflour, 1)
            sugar = round(ounces * rsugar, 1)
            baking_soda = round(ounces * rbaking_soda, 1)
            salt = round(ounces * rsalt, 1)
            cocoa_powder = round(ounces * rcocoa_powder, 1)
            canola_oil = round(ounces * rcanola_oil, 1)
            buttermilk = round(ounces * rbuttermilk, 1)
            egg = round(ounces * regg, 1)
            food_coloring = round(ounces * rfood_coloring, 1)
            vanilla_extract = round(ounces * rvanilla_extract, 1)
            distilled_vinegar = round(ounces * rdistilled_vinegar, 1)
            print("Regular Red Velvet Ingredient List:\nFlour:", flour, "Oz\nSugar:", sugar,
                  "Oz\nBaking Soda:", baking_soda, "Oz\nSalt:", salt, "Oz\nCocoa Powder:", cocoa_powder,
                  "Oz\nCanola Oil:", canola_oil, "Oz\nButtermilk:", buttermilk, "Oz\nEgg:", egg,
                  "Oz\nRed Food Coloring:", food_coloring, "Oz\nVanilla Extract:", vanilla_extract,
                  "Oz\nDistilled Vinegar:", distilled_vinegar, "Oz")
        if type == 3:
            butter = round(ounces * lbutter, 1)
            sugar = round(ounces * lsugar, 1)
            egg = round(ounces * legg, 1)
            flour = round(ounces * lflour, 1)
            buttermilk = round(ounces * lbuttermilk, 1)
            vanilla_extract = round(ounces * lvanilla_extract, 1)
            egg_yolk_filling = round(ounces * legg_yolk_filling, 1)
            sugar_filling = round(ounces * lsugar_filling, 1)
            butter_filling = round(ounces * lbutter_filling, 1)
            lemon_juice_zest_filling = round(ounces * llemon_juice_zest_filling, 1)
            print("Regular Lemon Ingredient List:\nButter:",butter,"Oz\nSugar:",sugar,"Oz\nEgg:",egg,"Oz\nFlour:",flour,
                  "Oz\nButtermilk:",buttermilk,
                  "Oz\nVanilla Extract:",vanilla_extract,"Oz\nEgg Yolk Filling:",egg_yolk_filling,"Oz\nSugar Filling:",sugar_filling,
                  "Oz\nButter Filling:",butter_filling,"Oz\nLemon Juice and Zest Filling:",lemon_juice_zest_filling,"Oz")
    elif size == "L":
        ounces = 112
        if type == 1:
            flour = round(ounces * cflour, 1)
            sugar = round(ounces * csugar, 1)
            cocoa = round(ounces * ccocoa, 1)
            baking_powder = round(ounces * cbaking_powder, 1)
            baking_soda = round(ounces * cbaking_soda, 1)
            salt = round(ounces * csalt, 1)
            egg = round(ounces * cegg, 1)
            butter_milk = round(ounces * cbutter_milk, 1)
            canola_oil = round(ounces * ccanola_oil, 1)
            vanilla_extract = round(ounces * cvanilla_extract, 1)
            boiling_water = round(ounces * cboiling_water, 1)
            print("Large Chocolate Ingredient List:\nFlour:", flour, "Oz\nSugar:", sugar, "Oz\nCocoa Powder:", cocoa,
                  "Oz\nBaking Powder:", baking_powder, "Oz\nBaking Soda:", baking_soda, "Oz\nSalt:", salt, "Oz\nEgg:",
                  egg, "Oz"
                       "\nButtermilk:", butter_milk, "Oz\nCanola Oil:", canola_oil, "Oz\nVanilla Extract:",
                  vanilla_extract,
                  "Oz\nBoiling Water:", boiling_water, "Oz")
        if type == 2:
            flour = round(ounces * rflour, 1)
            sugar = round(ounces * rsugar, 1)
            baking_soda = round(ounces * rbaking_soda, 1)
            salt = round(ounces * rsalt, 1)
            cocoa_powder = round(ounces * rcocoa_powder, 1)
            canola_oil = round(ounces * rcanola_oil, 1)
            buttermilk = round(ounces * rbuttermilk, 1)
            egg = round(ounces * regg, 1)
            food_coloring = round(ounces * rfood_coloring, 1)
            vanilla_extract = round(ounces * rvanilla_extract, 1)
            distilled_vinegar = round(ounces * rdistilled_vinegar, 1)
            print("Large Red Velvet Ingredient List:\nFlour:", flour, "Oz\nSugar:", sugar,
                  "Oz\nBaking Soda:", baking_soda, "Oz\nSalt:", salt, "Oz\nCocoa Powder:", cocoa_powder,
                  "Oz\nCanola Oil:", canola_oil, "Oz\nButtermilk:", buttermilk, "Oz\nEgg:", egg,
                  "Oz\nRed Food Coloring:", food_coloring, "Oz\nVanilla Extract:", vanilla_extract,
                  "Oz\nDistilled Vinegar:", distilled_vinegar, "Oz")
        if type == 3:
            butter = round(ounces * lbutter, 1)
            sugar = round(ounces * lsugar, 1)
            egg = round(ounces * legg, 1)
            flour = round(ounces * lflour, 1)
            buttermilk = round(ounces * lbuttermilk, 1)
            vanilla_extract = round(ounces * lvanilla_extract, 1)
            egg_yolk_filling = round(ounces * legg_yolk_filling, 1)
            sugar_filling = round(ounces * lsugar_filling, 1)
            butter_filling = round(ounces * lbutter_filling, 1)
            lemon_juice_zest_filling = round(ounces * llemon_juice_zest_filling, 1)
            print("Large Lemon Ingredient List:\nButter:", butter, "Oz\nSugar:", sugar, "Oz\nEgg:", egg, "Oz\nFlour:",
                  flour,
                  "Oz\nButtermilk:", buttermilk,
                  "Oz\nVanilla Extract:", vanilla_extract, "Oz\nEgg Yolk Filling:", egg_yolk_filling,
                  "Oz\nSugar Filling:", sugar_filling,
                  "Oz\nButter Filling:", butter_filling, "Oz\nLemon Juice and Zest Filling:", lemon_juice_zest_filling,
                  "Oz")

# inputs user for size and type and also uses sentinel to loop through
cake_type = input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: ")
while not(cake_type == 'q' or cake_type == 'Q'):
    cake_size = input("Please select cake size; Enter L for large, R for regular: ")
    recipe(cake_size, int(cake_type))
    cake_type = input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: ")

# recording of output
'''
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 2
Please select cake size; Enter L for large, R for regular: L
Large Red Velvet Ingredient List:
Flour: 25.1 Oz
Sugar: 25.1 Oz
Baking Soda: 0.8 Oz
Salt: 0.4 Oz
Cocoa Powder: 0.4 Oz
Canola Oil: 26.9 Oz
Buttermilk: 20.0 Oz
Egg: 10.1 Oz
Red Food Coloring: 2.4 Oz
Vanilla Extract: 0.3 Oz
Distilled Vinegar: 0.4 Oz
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: R
Regular Lemon Ingredient List:
Butter: 5.4 Oz
Sugar: 9.6 Oz
Egg: 5.8 Oz
Flour: 10.0 Oz
Buttermilk: 5.8 Oz
Vanilla Extract: 0.1 Oz
Egg Yolk Filling: 11.5 Oz
Sugar Filling: 7.2 Oz
Butter Filling: 1.3 Oz
Lemon Juice and Zest Filling: 7.3 Oz
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: L
Large Lemon Ingredient List:
Butter: 9.5 Oz
Sugar: 16.8 Oz
Egg: 10.1 Oz
Flour: 17.5 Oz
Buttermilk: 10.1 Oz
Vanilla Extract: 0.2 Oz
Egg Yolk Filling: 20.0 Oz
Sugar Filling: 12.7 Oz
Butter Filling: 2.4 Oz
Lemon Juice and Zest Filling: 12.8 Oz
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: R
Regular Chocolate Ingredient List:
Flour: 10.1 Oz
Sugar: 15.7 Oz
Cocoa Powder: 3.6 Oz
Baking Powder: 0.3 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Egg: 5.8 Oz
Buttermilk: 11.5 Oz
Canola Oil: 5.2 Oz
Vanilla Extract: 0.4 Oz
Boiling Water: 10.9 Oz
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: R
Regular Chocolate Ingredient List:
Flour: 10.1 Oz
Sugar: 15.7 Oz
Cocoa Powder: 3.6 Oz
Baking Powder: 0.3 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Egg: 5.8 Oz
Buttermilk: 11.5 Oz
Canola Oil: 5.2 Oz
Vanilla Extract: 0.4 Oz
Boiling Water: 10.9 Oz
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon, q to quit: Q

Process finished with exit code 0
'''
