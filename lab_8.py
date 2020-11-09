"""
***************************************************************************
Filename:      lab_8

Author:        Richa Bavadekar

Date:          12/1/19

Modifications: Richa Bavadekar - 12/1/19

Description:   This lab creates a class Cake with methods __init__, __self__, and calc_ingrd().
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
Classname:      cake

Author:        Richa Bavadekar

Date:          12/1/19

Modifications: Richa Bavadekar - 12/1/19

Description:   This class has methods __init__, __self__, and calc_ingrd().
***************************************************************************
"""
class Cake:
    """
    ***************************************************************************
    Function:   __init__(self, type, size)

    Parameters: type - type of cake
                size - size of cake

    Outputs: None

    Returns: None

    Author:  Richa Bavadekar

    Date:  12/1/19

    Modifications: 12/1/19

    Description: constructor method that initializes variables
    ***************************************************************************
    """
    def __init__(self, type, size):
        self.type = type
        self.size = size
        self.ingrd_list = []
        if type == 1:
            self.recipe = chocolate_recipe
            if size == 'R':
                self.name = 'Regular Chocolate Cake'
            else:
                self.name = 'Large Chocolate Cake'
        elif type == 2:
            self.recipe = red_velvet_recipe
            if size == 'R':
                self.name = 'Regular Red Velvet Cake'
            else:
                self.name = 'Large Red Velvet Cake'
        else:
            self.recipe = lemon_recipe
            if size == 'R':
                self.name = 'Regular Lemon Cake'
            else:
                self.name = 'Large Lemon Cake'

        if size == 'R':
            self.weight = 64
        else:
            self.weight = 112

    """
        ***************************************************************************
        Function:   __init__(self, type, size)

        Parameters: weight - weight of cake
                    recipe - dictionary

        Outputs: None

        Returns: ingredient list - list that contains all the names and ingredients for specific recipe 

        Author:  Richa Bavadekar

        Date:  12/1/19

        Modifications: 12/1/19

        Description: this method calculates the specific amount of ingredient for each type of cake
        ***************************************************************************
        """
    def calc_ingrd(self, weight, recipe):
        ingredient_list = []
        for key, value in recipe.items():
            ingredient = round(weight * value, 1)
            ingredient_list.append([key,ingredient])
        #print(ingredient_list)
        return ingredient_list

    """
        ***************************************************************************
        Function:   __self__(self, type, size)

        Parameters: none

        Outputs: prints out the ingredient quantities for each recipe 

        Returns: None

        Author:  Richa Bavadekar

        Date:  12/1/19

        Modifications: 12/1/19

        Description: this method is called when print() is called on an instance of this class
        ***************************************************************************
        """
    def __str__(self):
        s = "Ingredient Quantities for " + self.name + ":"
        list1 = self.calc_ingrd(self.weight, self.recipe)
        for i in list1:
            s += "\n" + i[0] + ": " + str(i[1]) + " Oz"
        return s

lemon_large = Cake(3, 'L')
print(lemon_large)
lemon_regular = Cake(3, 'R')
print(lemon_regular)

red_velvet_large = Cake(2, 'L')
print(red_velvet_large)
red_velvet_regular = Cake(2, 'R')
print(red_velvet_regular)

chocolate_large = Cake(1, 'L')
print(chocolate_large)
chocolate_regular = Cake(1, 'R')
print(chocolate_regular)

'''
Recording of output:

Ingredient Quantities for Large Lemon Cake:
Butter: 9.5 Oz
Sugar: 16.8 Oz
Egg: 10.1 Oz
Sifted Self-Rising Flour: 17.5 Oz
Buttermilk: 10.1 Oz
Vanilla Extract: 0.2 Oz
Egg Yolk Filling: 20.0 Oz
Sugar Filling: 12.7 Oz
Butter Filling: 2.4 Oz
Lemon Juice and Zest Filling: 12.8 Oz
Ingredient Quantities for Regular Lemon Cake:
Butter: 5.4 Oz
Sugar: 9.6 Oz
Egg: 5.8 Oz
Sifted Self-Rising Flour: 10.0 Oz
Buttermilk: 5.8 Oz
Vanilla Extract: 0.1 Oz
Egg Yolk Filling: 11.5 Oz
Sugar Filling: 7.2 Oz
Butter Filling: 1.3 Oz
Lemon Juice and Zest Filling: 7.3 Oz
Ingredient Quantities for Large Red Velvet Cake:
Flour: 25.1 Oz
Sugar: 25.1 Oz
Baking Soda: 0.8 Oz
Salt: 0.4 Oz
Unsweetened Cocoa Powder: 0.4 Oz
Canola Oil: 26.9 Oz
Buttermilk: 20.0 Oz
Egg: 10.1 Oz
Red Food Coloring: 2.4 Oz
Vanilla Extract: 0.3 Oz
Distilled Vinegar: 0.4 Oz
Ingredient Quantities for Regular Red Velvet Cake:
Flour: 14.3 Oz
Sugar: 14.3 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Unsweetened Cocoa Powder: 0.3 Oz
Canola Oil: 15.4 Oz
Buttermilk: 11.5 Oz
Egg: 5.8 Oz
Red Food Coloring: 1.3 Oz
Vanilla Extract: 0.2 Oz
Distilled Vinegar: 0.3 Oz
Ingredient Quantities for Large Chocolate Cake:
Flour: 17.7 Oz
Sugar: 27.4 Oz
Unsweetened Cocoa Powder: 6.3 Oz
Baking Powder: 0.4 Oz
Baking Soda: 0.7 Oz
Salt: 0.4 Oz
Egg: 10.1 Oz
Buttermilk: 20.2 Oz
Canola Oil: 9.1 Oz
Vanilla Extract: 0.7 Oz
Boiling Water: 19.0 Oz
Ingredient Quantities for Regular Chocolate Cake:
Flour: 10.1 Oz
Sugar: 15.7 Oz
Unsweetened Cocoa Powder: 3.6 Oz
Baking Powder: 0.3 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Egg: 5.8 Oz
Buttermilk: 11.5 Oz
Canola Oil: 5.2 Oz
Vanilla Extract: 0.4 Oz
Boiling Water: 10.9 Oz

Process finished with exit code 0

'''








