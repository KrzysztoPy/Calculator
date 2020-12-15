from MainMenuGui import welcome_main_menu_gui
from InputOperation.GetOperation import input_operation
from PerformationTheOperation.ExecutionTheOperation import execution_operation


def main_menu():
    welcome_main_menu_gui()
    execution_operation(input_operation())


main_menu()
