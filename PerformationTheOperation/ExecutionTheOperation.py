from InputOperation.GetOperationGui import view_available_operation_gui, abbreviation_list_gui
from InputOperation.GetOperation import get_operation


def help_option():
    view_available_operation_gui()
    get_operation()


def check_operation(operation):
    abbreviation_list = abbreviation_list_gui()
    # (1+1-1*(3/14))
    for counter in range(0, operation.__len__()):
        operation[counter] == '(' or operation[counter] == ')'
    print()


def execution_operation(operation):
    if operation.lower() == '-help':
        help_option()
    else:
        check_operation(operation)
