# This is a sample Python script to be used in a Rivery logic step.

# Import variables from Rivery logic river environment.
from rivery_variables import variable_name_1, variable_name_2, variable_name_3


def print_variables(variable_name_1, variable_name_2, variable_name_3):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Rivery python script executing with supplied inputs: /'
          f'variable_name_1: {variable_name_1},'
          f'variable_name_2: {variable_name_2},'
          f'f variable_name_3: {variable_name_3}')


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_variables(variable_name_1,
                    variable_name_2,
                    variable_name_3)
