from bs4 import BeautifulSoup
import requests
def universal_selector(url, stuff):
    soup = [str(x) for x in BeautifulSoup(requests.get(url).content, features="html.parser").select(stuff)]
    return soup