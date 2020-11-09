"""
***************************************************************************
Filename:      lab_9.py

Author:        Richa Bavadekar

Date:          12/7/19

Modifications: Richa Bavadekar - 12/7/19

Description:   This lab gets the max and min lenghts from a list of names, appends a new name based on
the users input, and finds all the names that have the same length that the user has chosen
***************************************************************************
"""

"""
***************************************************************************
Function:   get_length(min_length, max_length)

Parameters: min_length - min length
            max_length - max length

Outputs: None 

Returns: length of name inputted by user

Author:  Richa Bavadekar 

Date:  12/7/19

Modifications: 12/7/19

Description: This function gets the user inputted length. Keeps on prompting user if length is not betwwen min
and max lengths
***************************************************************************
"""
def get_length(min_length, max_length):
    name_length = int(input("What name length would you like? "))
    while not(name_length >= min_length and name_length <= max_length):
        name_length = int(input("What name length would you like? "))
    return name_length

"""
***************************************************************************
Function:   print_names(length)

Parameters: length - gotten from function get_length

Outputs: List of names from name_list that are equal in length to inputted length 

Returns: None

Author:  Richa Bavadekar 

Date:  12/7/19

Modifications: 12/7/19

Description: This function prints the list of names from name_list that are equal in length to inputted length. 
***************************************************************************
"""
def print_names(length):
    name_list = open("lab9_input.txt")
    name_counter = 0
    print("Name(s) with length " + str(length) + ":\n")
    for line in name_list:
        if len(line.strip()) == length:
            name_counter += 1
            print(line)
    if name_counter == 0:
        print("None")
    name_list.close()

"""
***************************************************************************
Function:  add_name(min_length, max_length)

Parameters: min_length - min length
            max_length - max length

Outputs: None 

Returns: None

Author:  Richa Bavadekar 

Date:  12/7/19

Modifications: 12/7/19

Description: This function adds a name to the txt file. 
***************************************************************************
"""
def add_name(min_length, max_length):
    name_to_add = input("Enter a name with length between " + str(min_length) + " and  " + str(max_length) + ": ")
    if len(name_to_add) < min_length or len(name_to_add) > max_length:
        add_name(min_length, max_length)

    name_list = open("lab9_input.txt", 'a')
    name_list.write("\n" + name_to_add)
    name_list.close()

"""
***************************************************************************
Function:  main()

Parameters: None

Outputs: The number of names in the list, the shortest name lenght, and the longest name length

Returns: None

Author:  Richa Bavadekar 

Date:  12/7/19

Modifications: 12/7/19

Description: This function prints the number of names in the list, the shortest name length, and the longest name length. 
***************************************************************************
"""
def main():
    name_list = open("lab9_input.txt")
    num_of_names = 0
    small_name = " " * 1000
    big_name = " "
    for line in name_list:
        num_of_names += 1
        if (len(line) < len(small_name)):
            small_name = line.strip()
        if (len(line) > len(big_name)):
            big_name = line.strip()
    name_list.close()

    min_length = len(small_name.strip())
    max_length = len(big_name.strip())


    print("There are " + str(num_of_names) + " names in the class list.")
    print("The shortest name has " + str(min_length) + " characters.")
    print("The longest name has " + str(max_length) + " characters.")
    add_name(min_length, max_length)


    while (True):
        name_length = get_length(min_length, max_length)
        print_names(name_length)
        user_continue = input("Continue? Y or N: ")
        if user_continue.lower() == 'n':
            break

#calling main
main()

#recording of output
'''
There are 44 names in the class list.
The shortest name has 3 characters.
The longest name has 10 characters.
Enter a name with length between 3 and  10: Richa
What name length would you like? 2
What name length would you like? 77
What name length would you like? 5
Name(s) with length 5:

Aaron

Aarti

Adiam

Brian

Chris

David

David

Ercan

Jimmy

Kelly

Priya

YuWen

Richa
Continue? Y or N: N

Process finished with exit code 0
'''





