import json

f = open("raw_aurin_data/melb_income.json")
raw_income = json.load(f)

greater_melb_geojson = json.load(open('./geojson/greater_melb_sub.json'))
au_suburbs_name = [i['properties']['name'].lower()for i in greater_melb_geojson["features"]]

raw_income_lst = []
for i in range(len(raw_income['features'])):
    data = raw_income['features'][i]['properties']
    loc = data['sa2_name_2016'].split('-')[0].strip().lower()
    if loc in au_suburbs_name:
        raw_income_lst.append(data)

income_lst = []
for i in range(len(raw_income_lst)):
    location = raw_income_lst[i]['sa2_name_2016'].split('-')[0].strip()
    per_mean_ttl_income = raw_income_lst[i]['estimates_personal_income_year_ended_30_june_mean_employee']
    per_median_ttl_income = raw_income_lst[i]['estimates_personal_income_year_ended_30_june_median_employee']
    if per_median_ttl_income and per_mean_ttl_income:
        income_lst.append({'Location':location,'Personal mean total income':per_mean_ttl_income,'Personal median total income':per_median_ttl_income})

au_income_json = json.dumps(income_lst,sort_keys=True, indent=4, separators=(',', ': '))
path = './result_aurin_data/result_melb_income.json'
file = open(path, 'w')
file.write(au_income_json)
file.close()