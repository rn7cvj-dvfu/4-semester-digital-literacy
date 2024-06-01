import os
import random
from faker import Faker
from datetime import datetime, timedelta
from docxtpl import DocxTemplate

fake = Faker()


address = fake.address().replace('\n', ', ')


date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%d.%m.%Y")
time = (datetime.now() + timedelta(minutes=random.randint(1, 1440))).strftime("%H:%M")

data = [fake.name() for i in range(10)]

# Загружаем шаблон документа
tpl = DocxTemplate('invitation_template.docx')

path = "./result"
os.makedirs(path, exist_ok=True)

for i, name in enumerate(data):
    context = {'ФИО': name, 'Место': address, 'Время': time, 'Дата': date, 'Адрес': address}
    tpl.render(context)
    tpl.save(f'./result/{name.replace(" " , "_")}.docx')