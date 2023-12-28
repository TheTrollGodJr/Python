import openpyxl
import csv
import re

def get_path(filePath):
    filePath = filePath[::-1].split("/", 1)[1][::-1] + "/"
    return filePath

def extract_data_from_excel(input_file, output_file):
    wb = openpyxl.load_workbook(input_file)
    sheet = wb.active

    with open(output_file, 'w', encoding="utf-8") as output:
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value is not None:
                    output.write(f"Cell {cell.coordinate}: {cell.value}\n")

def sortCells(data):
    print(f"\n\n{data}\n\n")
    def custom_sort_key(cell):
        match = re.match(r'Cell ([A-Z]+)(\d+): (.+)', cell)
        if match:
            letter, number, data = match.groups()
            return letter, int(number)
        return cell
    sorted_data = sorted(data, key=custom_sort_key)
    for i in range(len(sorted_data)):
        sorted_data[i] = sorted_data[i] + "\n"
    print(f"{sorted_data}\n\n")
    return sorted_data

def extract_data_from_csv(input_file, output_file):
    cells = []
    with open(input_file, 'r', encoding="utf-8") as csv_file, open(output_file, 'w', encoding="utf-8") as output:
        reader = csv.reader(csv_file)
        for row_num, row in enumerate(reader, start=1):
            for col_num, value in enumerate(row, start=1):
                if value:
                    cells.append(f"Cell {chr(64 + col_num)}{row_num}:{value}")
                    #output.write(f"Cell {chr(64 + col_num)}{row_num}: {value}\n")
        data = sortCells(cells)
        for items in data:
            output.write(items)
        #for items in cells:
        #    output.write(f"{items}, ")


file = "C:/Users/thetr/Documents/Python/spreadSheetAnalyzer/files/2023-24-Tournament-Schedule.csv"
extract_data_from_csv(file, f"{get_path(file)}output.txt")



#C:/Users/thetr/Documents/Python/spreadSheetAnalyzer/files/Shadian.csv