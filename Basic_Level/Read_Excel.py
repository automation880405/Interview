import pandas as pd

# Load the Excel file
import pandas as pd

# Load the Excel file
file_path = "C:/Users/avina/Desktop/read.xlsx"  # Replace with your file path
df = pd.read_excel(file_path,header=None)

# Read and print all rows and columns
total_rows, total_columns = df.shape

print("All Values in the Excel File:")
for row in range(total_rows):
    for col in range(total_columns):
        print(df.iloc[row, col], end="\t")  # Tab-separated values
    print()  # Newline after each row