import csv

def convert_json_to_csv(file):
    import json
    # Opening JSON file
    f = open(file + '.json',)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    print(data)
    for i in data['emp_details']:
        print(i)
    
    # Closing file
    f.close()
    pass

convert_json_to_csv('java')
convert_json_to_csv('python')
convert_json_to_csv('node')