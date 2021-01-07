from PerformationTheOperation.ExecutionTheOperation import execution_operation
from InputOperation.GetOperationGui import full_name_operation_gui, abbreviation_list_gui
from PerformationTheOperation.ExecutionTheOperationGui import *
from PerformationTheOperation.ExecutionTheOperation import *


def execution_operation_test():
    # result = execution_operation('-HelP')
    # result == full_name_operation_gui() + abbreviation_list_gui()
    test_object = '(2 * (2 - 1 * (3 / 14)))'
    # result = execution_operation(test_object)

    # test_object = '(2 * (2 - 1 * (3 / ))14'
    # print(test_object.replace(' ', ''))
    # result = remove_last_close_parenthesis(test_object)
    # print(result)
    # test_operation = '24-56'
    # result = operations_on_action(test_operation)
    # print(result)
    # operation = '24+12-4124*123/412-10%'
    # result = find_sign(operation)
    # print()

    operation = '-21-*2*(2-1)(3/1))(*23)ln(10)+l(10)-s(10)'
    operation = '-())+(()))+()()'
    result = find_sign(operation)

    lista = [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]

    for i in range(0, lista.__len__()):
        pass



execution_operation_test()
