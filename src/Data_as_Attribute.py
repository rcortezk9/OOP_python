"""In this one, we will cook the data into our class, as an instance variable. This is so that we can do fancy things
later, such as renaming columns, as well as getting descriptive statistics. """

# Import numpy as np, pandas as pd
import numpy as np
import pandas as pd


# Create class: DataShell
class DataShell:

    # Define initialization method
    def __init__(self, filepath):
        # Set filepath as instance variable
        self.filepath = filepath
        # Set data_as_csv as instance variable
        self.data_as_csv = pd.read_csv(filepath)

    # Define method rename_column, with arguments self, column_name, and new_column_name
    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)

    # Define get_stats method, with argument self
    def get_stats(self):
        # Return a description data_as_csv
        return self.data_as_csv.describe()


# Instantiate DataShell as us_data_shell
us_data_shell = DataShell('us_life_expectancy.csv')

# Print the datatype of your object's data_as_csv attribute
print(us_data_shell.data_as_csv.dtypes)

# Rename your objects column 'code' to 'country_code'
us_data_shell.rename_column('code', 'country_code')

# Again, print the datatype of your object's data_as_csv attribute
print(us_data_shell.data_as_csv.dtypes)

# Print the output of your objects get_stats method
print(us_data_shell.get_stats())