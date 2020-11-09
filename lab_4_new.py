"""
***************************************************************************
Filename:      lab_4.py

Author:        Richa Bavadekar

Date:          11/11/19

Modifications: Richa Bavadekar - 11/11/19

Description:   This lab takes in user input for type of cake and size of cake, and prints out the ounces of each
               ingredient accordingly.
***************************************************************************
"""

# chocolate cake ingredient percentages divided by 100
ca = 0.158
cb = 0.245
cc = 0.056
cd = 0.541

# red velvet cake ingredient percentages divided by 100
ra = 0.224
rb = 0.224
rc = 0.240
rd = 0.179
re = 0.133

# lemon cake percentages divided by 100
la = 0.385
lb = 0.358
lc = 0.257

"""
***************************************************************************
Function:   recipe(size, type)

Parameters: size - string R or L to determine the size 
            type - number 1, 2, or 3 to determine cake type 

Outputs: string with each ingredient and how much of it in ounces to use for this specific cake recipe 

Returns: None

Author:  Richa Bavadekar 

Date:  11/11/19

Modifications: 11/11/19

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
            A = round(ounces * ca, 1)
            B = round(ounces * cb, 1)
            C = round(ounces * cc, 1)
            D = round(ounces * cd, 1)
            print("Regular Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C,
                  "Oz\nIngredient D:", D, "Oz")
        if type == 2:
            A = round(ounces * ra, 1)
            B = round(ounces * rb, 1)
            C = round(ounces * rc, 1)
            D = round(ounces * rd, 1)
            E = round(ounces * re, 1)
            print("Regular Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C,
                  "Oz\nIngredient D:", D, "Oz\nIngredient E:", E, "Oz")
        if type == 3:
            A = round(ounces * la, 1)
            B = round(ounces * lb, 1)
            C = round(ounces * lc, 1)
            print("Regular Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C, "Oz")
    elif size == "L":
        ounces = 112
        if type == 1:
            A = round(ounces * ca, 1)
            B = round(ounces * cb, 1)
            C = round(ounces * cc, 1)
            D = round(ounces * cd, 1)
            print("Large Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C, "Oz\nIngredient D:", D, "Oz")
        if type == 2:
            A = round(ounces * ra, 1)
            B = round(ounces * rb, 1)
            C = round(ounces * rc, 1)
            D = round(ounces * rd, 1)
            E = round(ounces * re, 1)
            print("Large Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C, "Oz\nIngredient D:", D, "Oz\nIngredient E:", E, "Oz")
        if type == 3:
            A = round(ounces * la, 1)
            B = round(ounces * lb, 1)
            C = round(ounces * lc, 1)
            print("Large Chocolate Ingredient List:\nIngredient A:", A, "Oz\nIngredient B:", B, "Oz\nIngredient C:",
                  C, "Oz")


# inputs user for size and type
cake_type = int(input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: "))
cake_size = input("Please select cake size; Enter L for large, R for regular: ")

# runs function with specified size and type
recipe(cake_size, cake_type)

# recording of output
'''
Large Chocolate Ingredient List:
Ingredient A: 17.7 Oz
Ingredient B: 27.4 Oz
Ingredient C: 6.3 Oz
Ingredient D: 60.6 Oz

Regular Chocolate Ingredient List:
Ingredient A: 24.6 Oz
Ingredient B: 22.9 Oz
Ingredient C: 16.4 Oz

Large Chocolate Ingredient List:
Ingredient A: 25.1 Oz
Ingredient B: 25.1 Oz
Ingredient C: 26.9 Oz
Ingredient D: 20.0 Oz
Ingredient E: 14.9 Oz

'''
