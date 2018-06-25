import os
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

def getPDF(chapter, location):
	os.system('wkhtmltopdf' )

def main():
    url = 'http://www.deeplearningbook.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    chapters_url = [urljoin(url, link.get('href')) for link in soup.select('li > a')]

    os.makedirs('./DeepLearning')

    chapter_no = 1
    for chapter in chapters_url:
    	r = requests.get(chapter)
    	soup = BeautifulSoup(r.text, 'lxml')   

    	print('Printing chapter no. {}'.format(chapter_no))
    	getPDF(chapter, './DeepLearning/{}.pdf'.format(chapter_no))
    	print('Printing Chapter {} complete'.format(chapter_no))
    	chapter_no += 1


if __name__ == '__main__':
    main()
