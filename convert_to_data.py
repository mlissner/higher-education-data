import csv
import json

schools = []

with open('./data/DOE/data-2009-2010.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    pk = 1
    for row in reader:
        school = {
            'pk': pk,
            'model': 'judges.School',
            'fields': {
                'name':    row['INSTNM'].decode('latin-1').strip(),
                'unit_id': int(row['UNITID'].decode('latin-1').strip()),
                'ein':     int(row['EIN'].decode('latin-1').strip()),
                'ope_id':  int(row['OPEID'].decode('latin-1').strip()),
            }
        }

        schools.append(school)
        root_pk = pk
        pk += 1
        clean_aliases = [alias.decode('latin-1').strip() for alias in
                         row['IALIAS'].split('|') if alias.strip()]
        for alias in clean_aliases:
            school = {
                'pk': pk,
                'model': 'judges.School',
                'fields': {
                    'name': alias,
                    'is_alias_of': root_pk,
                }
            }
            schools.append(school)
            pk += 1

with open('./school_data.json', 'wb') as out:
    json.dump(schools, out, indent=2)

