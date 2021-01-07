def user_manual_gui():
    print('''\n How to using this calculator, example: 
    1. Write example: -(1+5*3/15)
    2. press enter
    3. Check the result: -2
    4. If you need help write: -help''')


def full_name_operation_gui():
    full_name_operation = ['Addition', 'subtraction', 'multiplication', 'division', 'percent', 'exponentiation',
                           'square root', 'change of sign', 'brackets']
    return full_name_operation


def abbreviation_list_gui():
    abbreviation_list = ['+', '-', '*', '/', '^', '%', 's', 'l', 'ln', '!', '||', '()', '+/-']
    return abbreviation_list


def view_available_operation_gui():
    text_with_available_operation = ''
    full_name_operation = full_name_operation_gui()
    abbreviation_list = abbreviation_list_gui()

    for counter in range(0, full_name_operation.__len__()):
        text_with_available_operation += full_name_operation[counter] + ' use " ' + abbreviation_list[counter]
        if counter > 0 and counter % 5 == 0:
            text_with_available_operation += '\n'
        if counter == full_name_operation.__len__() - 1:
            text_with_available_operation += ' "\n'
        else:
            text_with_available_operation += ' ", '
    print('\n' + text_with_available_operation)


def hint():
    print('If you want again see table with individual operations write: "-help"')
