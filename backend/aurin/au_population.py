import json

f = open("raw_aurin_data/au_population.json")
raw_pop = json.load(f)

raw_pop_lst = []
for i in range(len(raw_pop['features'])):
    data = raw_pop['features'][i]['properties']
    raw_pop_lst.append(data)

pop_lst = []
for i in range(len(raw_pop_lst)):
    location = raw_pop_lst[i]['gccsa_name_2016']
    ttl_pop = raw_pop_lst[i]['estmtd_rsdnt_ppltn_smmry_sttstcs_30_jne_prsns_ttl_nm']
    ttl_male = raw_pop_lst[i]['estmtd_rsdnt_ppltn_smmry_sttstcs_30_jne_mls_ttl_nm']
    ttl_female = raw_pop_lst[i]['estmtd_rsdnt_ppltn_smmry_sttstcs_30_jne_fmls_ttl_nm']
    median_age = raw_pop_lst[i]['estmtd_rsdnt_ppltn_smmry_sttstcs_30_jne_mdn_age_prsns_yrs']

    age_proportion = {}
    age_proportion['0-9 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_0_4_years_pc"]+\
                                      raw_pop_lst[i]["estimated_resident_population_persons_30_june_5_9_years_pc"]
    age_proportion['10-19 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_10_14_years_pc"] + \
                                      raw_pop_lst[i]["estimated_resident_population_persons_30_june_15_19_years_pc"]
    age_proportion['20-29 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_20_24_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_25_29_years_pc"]
    age_proportion['30-39 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_34_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_35_39_years_pc"]
    age_proportion['40-49 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_40_44_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_45_49_years_pc"]
    age_proportion['50-59 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_50_54_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_55_59_years_pc"]
    age_proportion['60-69 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_60_64_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_65_69_years_pc"]
    age_proportion['70-79 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_70_74_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_75_79_years_pc"]
    age_proportion['80-89 years old'] = raw_pop_lst[i]["estimated_resident_population_persons_30_june_80_84_years_pc"] + \
                                        raw_pop_lst[i]["estimated_resident_population_persons_30_june_persons_85_pc"]

    pop_lst.append({'Location':location,'Total population':ttl_pop,'Total male':ttl_male,'Total female':ttl_female,
                    'Age proportion':age_proportion,'Median age':median_age})

au_income_json = json.dumps(pop_lst, indent=4, separators=(',', ': '))
path = './result_aurin_data/result_au_population.json'
file = open(path, 'w')
file.write(au_income_json)
file.close()