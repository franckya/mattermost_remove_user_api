import json
import requests
import os

#db_password= os.environ.get('mytoken')
mytoken = 'ACCESS_TOKEN'
apiurl = 'https://example.com/api/v4/'
page = 0
per_page = 100
fetch = 1
user_id = 'USER_ID_HERE'
channel_id = 'CHANNEL_ID_HERE'
final_url = "https://example.com/api/v4/channels/CHANNEL_ID_HEREc/members/USER_ID_HERE"

#final_url= base_url+'channel_id'+"/members"+'user_id'
while(fetch):
    r = requests.get(apiurl + '/channels?page=' + str(page) + '&per_page=' + str(per_page), headers={"Authorization": "Bearer " + mytoken})
    #print(r.status_code)
    data = r.json()
    #print(data)
    json_len = len(data)
    page = page + 1
    #print("Page " + str(page) + " Length: " + str(json_len))
    for record in data:
        #print(record['type'])
        if 'P' in record["type"]:
            r = requests.request("DELETE", final_url , headers={"Authorization": "Bearer " + mytoken});
            print(r.status_code)
            fetch = 0
            break;
