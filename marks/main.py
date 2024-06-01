import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', delimiter=',', header=None)

with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:

    for group, data in df.groupby(0):

        data.iloc[:, 3:] = data.iloc[:, 3:].apply(pd.to_numeric, errors='coerce')
        data['Average'] = data.iloc[:, 3:].mean(axis=1)
        
        data['Grade'] = pd.cut(data['Average'], bins=[0, 40, 50, 70, 80, 100], labels=[1 , 2, 3, 4, 5], right=False)

        data.to_excel(writer, sheet_name=group, index=False)
      
        workbook  = writer.book
        worksheet = writer.sheets[group]
      
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': 'Pie data',
            'categories': [group, 1, 0, len(data), 0],
            'values':     [group, 1, 1, len(data), 1],
        })
        worksheet.insert_chart('J2', chart1)
      
        chart2 = workbook.add_chart({'type': 'column'})
        chart2.add_series({
            'name':       'Histogram data',
            'categories': [group, 0, 2, 0, 9],
            'values':     [group, 1, 2, len(data), 9],
        })
      
        worksheet.insert_chart('J15', chart2)