import openpyxl
# Converting between column letters and numbers
# from openpyxl.cell import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook('example.xlsx')
print(wb.get_sheet_names()) # Deprecated function
print(wb.sheetnames) # The new function

# get_column_letter(900)