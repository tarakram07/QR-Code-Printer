

def check_code(code):
    """
    Check the given list containing the entered code for format issues, and replace correct parts with None.
    If the format is incorrect, an error message will be inserted instead.

    Args:
    code (list): a list of strings containing the entered code

    Returns:
    code (list): a list of strings representing error for format issues of the code
    """

    # checking material number
    if not(len(code[0]) == 8 and code[0].isnumeric()):
        code[0] = "Invalid Material Number"
    else:
        code[0] = None

    # checking function stand
    if not(len(code[1]) == 2 and code[1].isnumeric() and not code[1] == "00"):
        code[1] = "Invalid Function Stand"
    else:
        code[1] = None

    # checking serial number
    if not (len(code[4]) == 4 and code[4].isnumeric() and not code[4] == "0000"):
        code[4] = "Invalid Serial Number"
    else:
        code[4] = None

    # set date and manufacturer to None
    code[2] = None
    code[3] = None

    return code

def next_serial(code):
    """
    this function receive a code from the last created qr code. the last four digits are transformed into an integer
    and written in a variable. the serial number is increased by one and combined with the code string. the function
    returns the completed code.

    args:
    code (str): code of the last created qr code

    return:
    code (str): code of the next qr code with serial number increased by one
    """

    # write serial number as int into "serial"
    serial = int(code[-4:])

    # incremented by one
    serial += 1

    # return combined string
    return code[:-4] + f"{serial:04d}"



def check_repetition(repetition):
    """
    this function receive the wished number of printed qr codes as string. the value is checked if its numeric and
    between 1 and 20, transformed into an integer and returned.

    arg:
    repetition (str): receive user input

    return:
    repetition (int): returns user input checked and transformed to int
    """

    # check if repetition is numeric
    if not repetition.isnumeric():
        # if not the value is set to "1"
        repetition = 1

    # transformation to int
    repetition = int(repetition)

    # check if bigger then 20
    if repetition > 20:
        # if bigger value is set to "20"
        repetition = 20

    # check if smaller then one
    if repetition < 1:
        # if smaller value is set to "1"
        repetition = 1

    # return the checked value
    return repetition
