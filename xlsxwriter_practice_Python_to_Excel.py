# Python Excel

# https://xlsxwriter.readthedocs.io/

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook("GeroTest.xlsx")
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = {1: "a", 2: "b", 3: "c"}
# print(type(expenses))  # tuple

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in expenses.items():
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1


workbook.close()
