from docxtpl import DocxTemplate
import csv
import json
with open('judgment_data.txt', 'r') as f:
    list_data = f.read()
a = ','
list_data = list_data.replace(', ',a)
list_data = list_data.split(',')
list_data = list(list_data)
stage = list_data[0]
object = list_data[1]
price = list_data[2]
result = list_data[3]
place = list_data[4]

def get_context(stage, object, price, result, place):
    return {'стадия': stage, 'предмет': object, 'цена': price, 'результат': result,'инстанция': place}

def from_template(stage, object, price, result, place, template):
    template = DocxTemplate(template)
    context = get_context(stage, object, price, result, place)
    template.render(context)
    template.save(stage + '_judgment.doсх')

def generate_report(stage, object, price, result, place):
    template = 'judgment_doc.docx'
    document = from_template(stage, object, price, result, place, template)
generate_report(stage, object, price, result, place)

list_1 = [['stage','object','price','result','place'],['completed','refund','114 000','16.12.2019 total victory','the first']]

with open('judgment.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&')
    writer.writerows(list_1)

with open('judgment.csv') as m:
    reader = csv.reader(m, delimiter = '&')
    for row in reader:
        print(row)

dict = {'stage' : 'completed', 'object' : 'refund', 'price' : '114 000', 'result' : '16.12.2019 total victory','place' : 'the first'}

with open('judgment.json', 'w') as f:
    json.dump(dict, f)

with open('judgment.json') as f:
    data = json.load(f)
    print(data)