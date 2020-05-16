#pull back all of the orgs and then query the license date in all of those orgs.

import requests
import cred

base_url = 'https://api.meraki.com/api/v0/'
headers = {'X-Cisco-Meraki-API-Key': (cred.key), 'Content-Type': 'application/json'}


get_orgs_url = base_url + 'organizations'


get_orgs_response = requests.request("GET", get_orgs_url, headers=headers)
get_orgs_json = get_orgs_response.json()



print("*" * 20)



for z in get_orgs_json:
    org_id = z['id']
    get_admins_url = base_url + 'organizations/%s/admins' % org_id
    get_admins_response = requests.get(get_admins_url, headers=headers)
    get_admins_json = get_admins_response.json()
    print("*" * 20)
    print(z['name'])
    print("*" * 20)
    for x in get_admins_json:
        print(x['name'] + ' ' + x['email'])

