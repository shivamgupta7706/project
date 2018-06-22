import sys 
import csv
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

def main():

    url = 'http://codeforces.com/' 
    path = '/problemset/standings/page/'
    page = 1

    standings_url = urljoin(url, path)

    f = open('detailCF.csv', 'w')
    while True:
        standings_page_url = urljoin(standings_url, str(page))      
        try:
            r = requests.get(standings_page_url)
        except requests.exceptions.RequestException as e:
            print('No internet Connection')
            sys.exit(1)

        try:
            r.raise_for_status()
        except Exception as e:
            print(e)
            exit(1)

        content = BeautifulSoup(r.text, 'lxml').findAll('td')
        
        info = []
        
        for i in range(len(content)):
            if i % 3 == 0:
                info.append(content[i].get_text().strip())
            elif i % 3 == 1:
                info.append(content[i].get_text().strip())
                absoulte_url = urljoin(url, content[i].get_text().strip())
                info.append(absoulte_url)
            elif i % 3 == 2:
                info.append(content[i].get_text().strip())   
                writer = csv.writer(f)
                writer.writerow(info)
                info = [] 
        page += 1
    

if __name__ == '__main__':
    main()