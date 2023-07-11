from googleapiclient.discovery import build

def get_base_domain(university, department, api_key):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=f'{university} {department} site:.edu', cx='YOUR_CX').execute()
    url = res['items'][0]['link']
    base_domain = url.split('/')[2]
    return base_domain
