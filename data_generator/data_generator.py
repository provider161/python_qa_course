"""
Script opens file with data, extracts data and generates new data file with shuffled cells data
"""
import random

file_name = "data.csv"
new_file = "generated.csv"

with open(file_name, 'r') as f:
    file_data = [line.rstrip('\n') for line in f]

splitted_data = [line.split(',') for line in file_data]

# extracting data from columns
fio_list = []
city_list = []
credit_card_list = []
deposit_list = []
hypotec_list = []
for line in splitted_data:
    fio_list.append(line[0])
    city_list.append(line[1])
    credit_card_list.append(line[2])
    deposit_list.append(line[3])
    hypotec_list.append(line[4])

# removing duplicates
fio_list = list(set(fio_list))
city_list = list(set(city_list))
credit_card_list = list(set(credit_card_list))
deposit_list = list(set(credit_card_list))
hypotec_list = list(set(hypotec_list))

# generating new 100 lines of random data
new_file_data = []
for i in range(100):
    fio = random.choice(fio_list)
    city = random.choice(city_list)
    credit_card = random.choice(credit_card_list)
    deposit = random.choice(deposit_list)
    hypotec = random.choice(hypotec_list)
    new_data = [fio, city, credit_card, deposit, hypotec]
    new_file_data.append(','.join(new_data))

with open(new_file, 'w') as out:
    for line in new_file_data:
        out.write(f'{line}\n')
