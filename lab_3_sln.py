def indent( str, spaces ):
    """
    ***************************************************************************

    Function:   indent( str, spaces )

    Parameters: str    - string to be printed
                spaces - number of spaces to be indented for printing

    Outputs: print the string with indentation specified by parameter "spaces"

    Returns: None

    Author:  Victor Lau

    Date:    2019.02.10

    Modifications:

    Description:
    This function prints a string with a specified number of white spaces
    indented. The first parameter is a string literal or variable.
    The second parameter is the number of white space to be indented.

    ***************************************************************************
    """

    # this would put an extra white space to it; won't work
    #  print( spaces * " ", str )

    # use the formatting operator and * operator to indent the string
    print( "%s%s" % (spaces * " ", str ) )

    # print( spaces * " " + str ) # this would work too



def center( string, screen_width ):
    """
    ***************************************************************************

    Function:   center( string, screen_width )

    Parameters: string       - string to be centered
                screen_width - screen width to be used to calculate the space
                               to be indented for centering the string

    Outputs: None

    Returns:    indent_space - the number of white spaces to be indented
                               for centering the string

    Author:  Victor Lau

    Date:    2019.02.10

    Modifications:

    Description:
    This function perfomrs:
    1) take a string input and the width of the screen;
    2) calculate the number of white spaces need to be indented in order to
       print the string centered on the screen;
    3) call the indent() function to print the centered string
    4) return the number of white spaces indented

    ***************************************************************************
    """

    # calculate white spaces to be indented for centering the string
    indent_space = ( screen_width - len(string) ) // 2

    # print the string with the calculated indented spaces
    indent( string, indent_space)

    # return the number of white spaces indented
    return indent_space



def read_n_center_text():
    """
    ***************************************************************************

    Function:   read_n_center_text()

    Parameters: None

    Inputs:     1. string input from keyboard
                2. screen width

    Outputs:    1. [call center() to ]print the string input with proper number
                   of indentation to place it at the center of the screen
                2. print the indented spaces to make the string centered

    Returns: None

    Author:  Victor Lau

    Date:    2019.02.10

    Modifications:

    Description:
    This function perfomrs:
    1) query a string input
    2) query the screen width
    3) call the function center() to print the string input at the center of the
       screen and print the indented spaces for centering
    ***************************************************************************
    """

    # query string and screen width
    string_input = input( "Type Text String: ")
    screen_width_input = eval( input( "Enter Screen Width: ") )

    # call the function center() to print the string at the center of screen
    indented_spaces = center( string_input, screen_width_input )

    # print the number of white spaces which centers the string
    print( "Indented by: %i " % indented_spaces)



'''
*******************************************************************************
Program Starts Here -
*******************************************************************************
'''
read_n_center_text()
