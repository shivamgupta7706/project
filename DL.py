from weasyprint import HTML
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

def getHTML(soup):
	title = soup.find(class_='t m0 x0 h2 y1 ff2 fs1 fc0 sc0 ls0 ws0')	
	if title:	
		title_html = title.getText() + '.html'
		#title_pdf = title.getText() + '.pdf'
		with open('./DeepLearning/' + title_html, 'w') as f:
			print(soup, file=f)
			#HTML('./DeepLearning/' + title_html).write_pdf('./DeepLearning/' + title_pdf, zoom=90)
			print('{} completely saved'.format(title.getText()))

def main():
    url = 'http://www.deeplearningbook.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    chapters_url = [urljoin(url, link.get('href')) for link in soup.select('li > a')]
    chapters_url = chapters_url[3:-2]
    
    #os.makedirs('./DeepLearning')

    for chapter in chapters_url:
    	r = requests.get(chapter)
    	soup = BeautifulSoup(r.text, 'lxml')
    	getHTML(soup)
    	
    print('Done.')

if __name__ == '__main__':
    main()
