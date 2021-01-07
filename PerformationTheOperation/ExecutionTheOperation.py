from InputOperation.GetOperationGui import view_available_operation_gui, abbreviation_list_gui
from InputOperation.GetOperation import get_operation
from PerformationTheOperation.ExecutionTheOperationGui import different_number_parentheses_gui


def help_option():
    view_available_operation_gui()
    get_operation()


# 1. Sprawdzenie czy działanie jest napisane poprawnie.
# A) Jeśl nie, to pokazać prawdopodobne miejsce błędu
# B) Jeśli tak To wykonać działanie

# Zasady
# 1. Przed znakiem działania musi być liczba
# 2. Nie można dzielić przez zero
# 3. Nawiasy muszą być pozamykane
# 4. W trakcie działania musi pojawić się znak

def actions_available():
    '''

    +   - Dodawanie             2+1         x
    -   - Odejmowanie           2-1         x
    *   - Mnożenie              2*5         x
    /   - Dzielenie             2/1         x

    ^   - potęgowanie           2^2         x
    %   - procent               100-10%     x
    s   - pierwiastek z 2       s(10)       x
    l   - logarytm              l(10)       x
    ln  - logarytm naturalny    ln(10)      x
    !   - silnia                10!         x
    ||  - Wartość bezwzględna   |10|        x
    ()  - Nawiasy               (2+2)       x

    '''

    '''
    Zasady:
    
    A) +,-,*,/ Dodawanie:
        1) liczba + liczba  = wynik
        2) +liczba + liczba = wynik 
        3) liczba + liczba +
    wniosek: Po znaku musi być liczba, po dzieleniu trzeba sprwdzić czy liczba jest większa od 0 
    
    B) ^ , %
    
    Wniosek: Liczba ^,% liczba nie inaczej, może być w nawiasie 
    
    C) s,l,ln,!
    Wniosek: Musi być znak(liczba)
    
    D) || 
    Wniosek: Musi być |liczba|
    
    '''

    pass


def all_sytuatiom():
    '''
    1. Za dużo nawiasów otwierających
        A. (2*43(       -> (2*43)           - domniemanie                       - Prawda
        B. (2/43*21(    -> (2/43*21)        - domniemanie                       - Prawda
        C. (2/43(*21(   -> ???              - Błąd brak możliwości domniemania  - Fausz
        D. )2*43(
    '''
    pass


def execution_operation(operation):
    if operation.lower() == '-help':
        help_option()
    else:
        operations_on_action(operation)

        #     making_the_equation(operation)
        # else:
        #     different_number_parentheses_gui(operation)


def find_sign(operation):
    copy_operation = operation
    # operation = ['+', '-', '*', '/', '^']
    numbers = []
    signs = []

    memory_first_num = ''

    for position_in_operation in range(0, copy_operation.__len__()):
        try:
            int(copy_operation[position_in_operation])
            memory_first_num += copy_operation[position_in_operation]
        except:
            if memory_first_num:
                numbers.append([position_in_operation - 1, memory_first_num])
                memory_first_num = ''
            signs.append([position_in_operation, copy_operation[position_in_operation]])
        finally:
            continue

    print('operation', operation)
    print('numbers:', numbers)
    print('sings: ', signs)
    signs = check_bracket(signs)

    print(operation)
    print(combine_numbers_and_characters_into_one_string(signs, numbers))


def check_bracket(signs):
    copy_signs = signs
    open_bracket_wrong_position = []
    open_bracket_position = []
    counter_open_bracket = 0
    close_bracket_position = []
    close_bracket_wrong_position = []

    for position in range(0, copy_signs.__len__()):
        if copy_signs[position][1] == '(':
            counter_open_bracket += 1
            open_bracket_wrong_position.append(counter_open_bracket)
            open_bracket_position.append(copy_signs[position][0])
        elif copy_signs[position][1] == ')':
            if copy_signs[position][0] == 0:
                open_bracket_wrong_position.append(copy_signs[position][0])
                # Throw error: Initially closed parenthesis
                break
            else:
                if open_bracket_wrong_position:
                    open_bracket_wrong_position.pop()
                    close_bracket_position.append(copy_signs[position][0])
                else:
                    close_bracket_wrong_position.append(copy_signs[position][0])

    print('Open_bracket_position:', open_bracket_position)
    print('Open_bracket_wrong:', open_bracket_wrong_position)
    print('Close_bracket_position', close_bracket_position)
    print('Close_bracket_wrong', close_bracket_wrong_position)

    copy_signs = remove_wrong_bracket(signs, open_bracket_wrong_position, close_bracket_wrong_position)
    check_backed_bombing(open_bracket_position, close_bracket_position)
    return copy_signs


def remove_wrong_bracket(signs, open_bracket_wrong_position, close_bracket_wrong_position):
    if open_bracket_wrong_position:
        for number in open_bracket_wrong_position:
            for position in range(0, signs.__len__()):
                if number == signs[position][0]:
                    del signs[position]
                    break

    if close_bracket_wrong_position:
        for number in close_bracket_wrong_position:
            for position in range(0, signs.__len__()):
                if number == signs[position][0]:
                    del signs[position]
                    # close_bracket_wrong_position = [value - 1 for value in close_bracket_wrong_position]
                    # print(close_bracket_wrong_position)
                    break

        for number in close_bracket_wrong_position[::-1]:
            for position_signs in range(0, signs.__len__()):
                if signs[position_signs][0] > number:
                    signs[position_signs][0] -= 1
    print(signs)
    return signs


def check_backed_bombing(open_bracket_position, close_bracket_position):
    pass


def combine_numbers_and_characters_into_one_string(signs, numbers):
    numbers += [[13, 2]]
    signs += [i for i in numbers]
    tidy_signs_and_numbers = ''
    counter = 0
    for repeat in range(0, signs.__len__()):
        for position in range(0, signs.__len__()):
            if signs[position][0] == counter:
                counter += 1
                tidy_signs_and_numbers += signs[position][1]
                break
    return tidy_signs_and_numbers


def check_correct(operation):
    can_be_on_beginning = ['+', '-', 's', 'l', '|', '(']
    actions_allowed_between_operations = ['+', '-', '*', '/', '(', '|']
    before_and_after_must_be_number = ['*', '/', '^']
    before_must_be_a_number = ['%', '!']
    must_be_open_close_brackets_and_number_between = ['l', 's', 'ln']
    round_brackets_open = 0
    round_brackets_close = 0
    abs_brackets = 0

    copy_operation = operation
    allowed_start_character = None

    open = 1

    close = 1
    # -21*(2*(2-1)*(3/1))(*23)

    ##########################
    # NEW
    ##########################

    tmp_memory_partial_operations = ''
    partial_operations = []
    last_sign = ''

    if copy_operation.__len__() > 0:
        for sign in can_be_on_beginning:
            if copy_operation[0] == sign:
                # Throw error: Illegal character at the beginning of the operation
                pass
            else:
                if copy_operation[0] == '+':
                    copy_operation[0] = ''
                elif copy_operation[0] == '-':
                    for position_in_operation in range(1, copy_operation.__len__()):
                        try:
                            int(copy_operation[position_in_operation])
                            tmp_memory_partial_operations += copy_operation[position_in_operation]
                        except ValueError as e:
                            if not tmp_memory_partial_operations:
                                # Throw error: Illegal character at the beginning of the operation
                                pass
                            else:
                                partial_operations.append('-' + tmp_memory_partial_operations)
                            if copy_operation[position_in_operation] not in actions_allowed_between_operations:
                                # Throw error: Illegal character between operations
                                pass
                            else:
                                continue


    else:
        # Throw error: Operation can't be empty
        pass


def operations_on_action(operation):
    copy_operation = operation
    memory_if_log = ''
    temp_log_position = None

    number = []
    number_position = []
    is_number_flag = False

    add_sub_position = []
    mul_div_exp_position = []
    per_fac_position = []
    log_position = []
    square_position = []

    log_nat_position = []
    round_brackets_position_open = []
    round_brackets_position_close = []
    abs_brackets_position = []

    for position_in_operation in range(0, copy_operation.__len__()):
        try:
            int(copy_operation[position_in_operation])
            number.append(int(copy_operation[position_in_operation]))
            number_position.append(position_in_operation)
            is_number_flag = True
        except ValueError as e:
            pass

        finally:
            if is_number_flag:
                is_number_flag = False

            elif not is_number_flag:
                if copy_operation[position_in_operation] == '+' or copy_operation[position_in_operation] == '-':
                    add_sub_position.append(position_in_operation)
                    if memory_if_log and temp_log_position:
                        log_position.append(temp_log_position)
                    continue

                elif copy_operation[position_in_operation] == '*' or copy_operation[position_in_operation] == '/' or \
                        copy_operation[position_in_operation] == '^':
                    mul_div_exp_position.append(position_in_operation)
                    if memory_if_log and temp_log_position:
                        log_position.append(temp_log_position)
                    continue

                elif copy_operation[position_in_operation] == '%' or copy_operation[position_in_operation] == '!':
                    per_fac_position.append(position_in_operation)
                    if memory_if_log and temp_log_position:
                        log_position.append(temp_log_position)
                        memory_if_log = ''
                        temp_log_position = None
                    continue

                elif copy_operation[position_in_operation] == 'l':
                    memory_if_log == copy_operation[position_in_operation]
                    temp_log_position = position_in_operation
                    continue

                elif memory_if_log and copy_operation[position_in_operation] == 'n':
                    if memory_if_log:
                        position = str(temp_log_position) + str(position_in_operation)
                        log_nat_position.append(position)
                        memory_if_log = ''
                        temp_log_position = None
                        continue

                elif copy_operation[position_in_operation] == 's':
                    square_position.append(copy_operation[position_in_operation])
                    continue

                elif copy_operation[position_in_operation] == '(':
                    round_brackets_position_open.append(position_in_operation)
                    continue

                elif copy_operation[position_in_operation] == ')':
                    round_brackets_position_close.append(position_in_operation)
                    continue

                elif copy_operation[position_in_operation] == '|':
                    abs_brackets_position.append(position_in_operation)
                    continue

    return number, number_position


def check_parenthesis(operation):
    abbreviation_list = abbreviation_list_gui()
    # (2*43)*(2-1*(3/14)))
    # (2*43)*(2-1*(3/14)))
    # (2*43)*(2-1*(3/14)))
    # 23+34*23)
    # 23*(-34+23
    # (2*43)*(2-1*(3/14)))
    # (2*43)*(2-1*(3/14)))
    # (2*43)*(2-1*(3/14))*10)
    # /2-7
    # (2 * (2 - 1 * (3 / ))14
    # (2*(2-1)*(3/1))?*23?
    # (2*(2-1)*(3/1))??????*23
    #

    open_parenthesis = 0
    close_parenthesis = 0

    for counter in range(0, operation.__len__()):
        if operation[counter] == '(':
            open_parenthesis += 1
        elif operation[counter] == ')':
            close_parenthesis += 1
            if close_parenthesis > open_parenthesis:
                # Throw it error: Started operation from open parenthesis...
                pass

    if open_parenthesis == close_parenthesis:
        correctness_of_parentheses(operation)
    elif open_parenthesis > close_parenthesis:
        pass
    elif close_parenthesis - open_parenthesis <= 1:
        execute_operation(remove_last_close_parenthesis(operation))


# Throw it error: Too many close parenthesis


# Throw it error: To many open parenthesis can't know where typing want had open parenthesis...


def remove_last_close_parenthesis(operation):
    open_parenthesis = 0
    close_parenthesis = 0
    position_close_parenthesis = 0

    for counter in range(0, operation.__len__()):
        if operation[counter] == '(':
            open_parenthesis += 1
        elif operation[counter] == ')':
            close_parenthesis += 1
            position_close_parenthesis = counter

    wrong_operation = operation
    corrected_operation = operation[0:position_close_parenthesis] + operation[position_close_parenthesis + 1:]

    return corrected_operation


def execute_operation(operation):
    pass


def correctness_of_parentheses(operation):
    open_parenthesis = 0
    close_parenthesis = 0

    # (2*43)*(2-1*(3/14)))
    # (2*43)*(2-1*(3/14)))
    # 23+34*23)
    # 23*(-34+23
    # (2*43)*(2-1*(3/14)))
    # 3*((2*4,3)*(10*(2-1*(3/14))))
    # ((2-5)

    for counter in range(0, operation.__len__()):
        if operation[counter] == '(':
            open_parenthesis += 1
        elif operation[counter] == ')':
            close_parenthesis += 1
        elif close_parenthesis > open_parenthesis:
            return "more closing than opening parentheses "

    if open_parenthesis > close_parenthesis:
        return "more opening than closing parentheses "
    else:
        return True


def making_the_equation(operation):
    return operation.__float__()
