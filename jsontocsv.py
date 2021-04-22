import csv, json

def convert_json_to_csv(file):
    f = open(file + '.json',)
    
    records = json.load(f)
    with open(file + '.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['Entity Name', 'Patterns', 'Response'])
        for record in records:
            csv_writer.writerow(['', record['question'].encode('utf-8').strip(), record['answer'].encode('utf-8').strip()])
    f.close()

convert_json_to_csv('java')
convert_json_to_csv('python')
convert_json_to_csv('node')