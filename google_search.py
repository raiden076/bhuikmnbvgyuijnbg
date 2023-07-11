from googleapiclient.discovery import build
from duckduckgo_search import DDGS as dd
from itertools import islice


def get_base_domain_goog(university, department, api_key):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=f'{university} {department} site:.edu', cx='YOUR_CX').execute()
    url = res['items'][0]['link']
    base_domain = url.split('/')[2]
    return base_domain



def get_base_doamin(university, department, api_key):
    with dd() as d:
        bs_dm = []
        d_gen = d.text(f"{department} {university}", backend='lite')
        for r in islice(d_gen, 10):
          bs_dm.append(r['href'].split('/')[2])
        return bs_dm