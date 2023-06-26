import json

# Open the file and load the data
with open('data/data.json', 'r') as file:
    data_list = json.load(file)

# Compare serial_number count with statistics
for data in data_list:
    serial_numbers = set(data['serial_number'].split(','))
    unique_serial_count = len(serial_numbers)
    statistics = data['statistics']
    if unique_serial_count == statistics:
        continue
    else:
        print('Serial count does not match statistics for batch {}'.format(data['batch']))