## https://gist.githubusercontent.com/cc1c/de6d8c12d619796b86ce02c5beb27461/raw/61b87185c52c7b19995c8c817b1f1e75946dd206/2_access_log.json

import requests
import pandas

response = requests.get("https://gist.githubusercontent.com/cc1c/de6d8c12d619796b86ce02c5beb27461/raw/61b87185c52c7b19995c8c817b1f1e75946dd206/2_access_log.json")
json_list = response.json()
login_list = []
sus_users = []
sus_logins = []

for item in json_list:
    UPN = item["email"]
    IP = item["ip_address"]
    URL = item["url"]
    logins = [UPN, IP, URL]
    login_list.append(logins)

login_df = pandas.DataFrame(login_list, columns=['UPN', 'IP', 'URL'])
login_df.drop('URL', axis=1, inplace=True)
login_df.drop_duplicates(subset=['UPN', 'IP'], inplace=True)
count_by_upn = login_df['UPN'].value_counts()
count_df = pandas.DataFrame(count_by_upn)
# Solution is found here, but why stop now.. 🙃
#print(count_df)

for index, row in count_df.iterrows():
    if row["count"] > 1:
        sus = index
        sus_users.append(sus)

for logins in login_list:
    if logins[0] in sus_users:
        if logins not in sus_logins:
            sus_logins.append(logins)

print(sus_logins)
