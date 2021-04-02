import xlrd

info = "main.xlsx"

inputWorkBook = xlrd.open_workbook(info)
inputWorkSheet = inputWorkBook.sheet_by_index(0)

print(inputWorkSheet.nrows)
print(inputWorkBook.ncols)
