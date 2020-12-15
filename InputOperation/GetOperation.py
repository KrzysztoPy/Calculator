from InputOperation.GetOperationGui import *
from GetOperationGui import full_name_operation_gui, abbreviation_list_gui


def get_operation():
    return input('Provide operation: ')


def input_operation():
    user_manual_gui()
    view_available_operation_gui()
    hint()
    return get_operation()
