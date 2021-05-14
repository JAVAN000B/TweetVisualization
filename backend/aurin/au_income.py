import json

f = open("raw_aurin_data/au_income.json")
raw_income = json.load(f)

raw_income_lst = []
for i in range(len(raw_income['features'])):
    data = raw_income['features'][i]['properties']
    raw_income_lst.append(data)

income_lst = []
for i in range(len(raw_income_lst)):
    location = raw_income_lst[i]['gccsa_name_2016']
    per_mean_ttl_income = raw_income_lst[i]['estimates_personal_income_year_ended_30_june_mean_employee']
    per_median_ttl_income = raw_income_lst[i]['estimates_personal_income_year_ended_30_june_median_employee']
    if per_median_ttl_income and per_mean_ttl_income:
        income_lst.append({'Location':location,'Personal mean total income':per_mean_ttl_income,'Personal median total income':per_median_ttl_income})

au_income_json = json.dumps(income_lst,sort_keys=True, indent=4, separators=(',', ': '))
path = './result_aurin_data/result_au_income.json'
file = open(path, 'w')
file.write(au_income_json)
file.close()