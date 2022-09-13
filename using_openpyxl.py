import openpyxl
# Converting between column letters and numbers
# from openpyxl.cell import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook('example.xlsx')
# print(wb.get_sheet_names()) # Deprecated function
print(wb.sheetnames) # The new function

# get_column_letter(900)

# Getting rows and columns from the sheets
# sheet = wb.get_sheet_by_name('Sheet1') #Deprecated
sheet = wb['Sheet1']
tuple(sheet['A1':'C3'])
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

# Writing to a file
# resultFile = open('census2010.py', 'w')
# resultFile.write('allData = ' + pprint.pformat(countyData))

# Creating a new blank workbook object
# openpyxl.Workbook()

# Creating and removing sheets
# use create_sheet() and remove_sheet() functions

# using different fonts in excel files
# from openpyxl.styles import Font, Style