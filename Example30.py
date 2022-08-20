"""DataDriving testing (from exel on local computer)
lessons 46 / Scenario 23 """

import xlrd

loc = ("/Users/Igor/Desktop/Разное/Python/Pairwise")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

p1 = sheet.cell(0, 0).value
print(p1)
