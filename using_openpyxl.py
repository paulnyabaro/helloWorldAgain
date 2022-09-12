import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(wb.get_sheet_names()) # Deprecated function
print(wb.sheetnames) # The new function