import openpyxl # type: ignore

# Open the Excel file
try:
  workbook = openpyxl.load_workbook(filename="Data HUMIC 2024.xlsx")
except FileNotFoundError:
  print("Error: The file 'Data HUMIC 2024.xlsx' does not exist.")
  exit()

# Get all worksheet names
worksheet_names = workbook.sheetnames

# Print each worksheet name
for sheet_name in worksheet_names:
  print(sheet_name)