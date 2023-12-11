import pandas as pd
import numpy as np
from faker import Faker

# Set a seed for reproducibility
np.random.seed(42)

# Create a Faker instance
fake = Faker()

# Define the number of rows and columns
num_rows = 50
num_columns = 11

# Generate random data with original column names
data = {
    f'Column{i+1}': np.random.randint(1, 100, num_rows) for i in range(num_columns)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Change the names of the columns
new_column_names = ['S_N', 'Client_Name', 'Gender', 'Age', 'Land_Area', 'Location', 'Contact_Number', 'Design_Type', 'Design/Construction', 'Attitude', 'Remarks']
df.columns = new_column_names

# Generate sequential serial numbers for the "S_N" column
df['S_N'] = np.arange(1, num_rows + 1)

# Generate random names for the "Client_Name" column (two words)
df['Client_Name'] = [fake.name() for _ in range(num_rows)]

# Generate random single-word locations for the "Location" column
df['Location'] = np.random.choice(['KMC', 'BKT', 'LMC', 'CMC', 'BMC'], size=num_rows)
# Generate random phone numbers with fixed prefix (984)
df['Contact_Number'] = ['984' + '{:07}'.format(np.random.randint(0, 9999999)) for _ in range(num_rows)]

# Generate random options for the "Gender" column
df['Gender'] = np.random.choice(['Male', 'Female', 'Other'], size=num_rows)

# Generate random options for the "Design_Type" column
df['Design_Type'] = np.random.choice(['Modern', 'Neo-Classical', 'Mixed', 'Traditional'], size=num_rows)

# Generate random options for the "Design/Construction" column
df['Design/Construction'] = np.random.choice(['Design Only', 'Construction Only', 'Both'], size=num_rows)

# Generate random options for the "Attitude" column
df['Attitude'] = np.random.choice(['Arrogant', 'Wise', 'Polite', 'Confident', 'Egotistical'], size=num_rows)

# Generate random ages between 25 and 65 for the "Age" column
df['Age'] = np.random.randint(25, 66, num_rows)

# Generate random land areas
df['Land_Area'] = [f'{np.random.randint(3, 12)} Anna' for _ in range(num_rows)]

# Fill the "Remarks" column with empty strings
df['Remarks'] = ''

# Specify the Excel file path
excel_file_path = r"C:\Users\nativ\Desktop\Coding With Rehan\Projects\random_data.xlsx"

# Write the DataFrame to an Excel sheet with adjusted column widths
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get the xlsxwriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set column widths (adjust these values as needed)
    column_widths = [5, 25, 8, 5, 10, 15, 15, 15, 20, 10, 10]  # Change these values as needed for each column
    for i, width in enumerate(column_widths):
        worksheet.set_column(i, i, width)

print("Random data with updated column names, widths, and information has been written to Excel successfully.")

