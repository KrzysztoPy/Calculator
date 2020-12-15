from PerformationTheOperation.ExecutionTheOperation import execution_operation
from InputOperation.GetOperationGui import full_name_operation_gui, abbreviation_list_gui


def execution_operation_test():
    result = execution_operation('-HelP')
    result == full_name_operation_gui() + abbreviation_list_gui()


execution_operation_test()
