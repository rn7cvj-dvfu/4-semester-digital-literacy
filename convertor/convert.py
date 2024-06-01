import argparse
import csv
import xlsxwriter

parser = argparse.ArgumentParser(description='Convert CSV to XLSX.')
parser.add_argument('input_file', type=str, help='Input CSV file name')
parser.add_argument('output_file', type=str, help='Output XLSX file name')
parser.add_argument('-d', '--delimiter', type=str, default=';', help='CSV delimiter')

args = parser.parse_args()

with open(args.input_file, 'r') as csv_file:
    workbook = xlsxwriter.Workbook(args.output_file)
    worksheet = workbook.add_worksheet()

    reader = csv.reader(csv_file, delimiter=args.delimiter)
    for i, row in enumerate(reader):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    workbook.close()