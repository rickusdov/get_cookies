import json
def fix_structure(data_dict):
    # Opening JSON file
    f = open('test.json')
    test_dict = json.load(f)
    f.close()
    cookies = ''
    for dict in test_dict:
        for dict2 in data_dict:
            if dict['name'] == dict2['name']:
                if 'expirationDate' in dict.keys():
                    dict['expirationDate'] = dict2['expirationDate']
                dict['value'] = dict2['value']
        cookies += str(dict) + ','
    return cookies
