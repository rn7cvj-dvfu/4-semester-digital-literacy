import random
import os
from docxtpl import DocxTemplate

data = [(f'Company {i}', f'Check {i}', f'Day {i}', f'Month {i}', f'Year {i}', f'Seller {i}', f'Address {i}', f'ORGN {i}', 
         [{'title': f'Product {j}', 'code': f'Code {j}', 'unit': f'Unit {j}', 'amount': random.randint(1, 100), 'price': random.randint(1, 100), 'sum': random.randint(1, 100)} for j in range(15)], 
         random.randint(1, 100)) for i in range(15)]

tpl = DocxTemplate('template.docx')

path = "./result"
os.makedirs(path, exist_ok=True)

for i, (company, check_number, day, month, year, seller, address, ORGN, products, general_sum) in enumerate(data):
    context = {'company': company, 'check_number': check_number, 'day': day, 'month': month, 'year': year, 'seller': seller, 'address': address, 'ORGN': ORGN, 'products': products, 'general_sum': general_sum}
    tpl.render(context)
    tpl.save(f'./result/document_{i}.docx')