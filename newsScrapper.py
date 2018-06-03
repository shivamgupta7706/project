import requests
from bs4 import BeautifulSoup

def printingNews(topic, allNews):
	print('Current news in the {}\n'.format(topic.capitalize()))
	for i in range(len(allNews)):
		print(str(i+1) + '- ',allNews[i] + '.')
	print()

def getNews(topic):

	url = 'http://zeenews.india.com/' + topic
	try:
		response = requests.get(url)
	except requests.exceptions.RequestException as e:
		print('No Internet Connection')
		exit(1)
	soup = BeautifulSoup(response.text, 'lxml')
	news = []
	for khabar in soup.findAll('h3'):
		if (khabar.text).strip() != '':
			news.append((khabar.text).strip().replace('\n', ': '))

	return news


def main():

	topics = ['cricket', 'business', 'technology', 'world']

	for topic in topics:
		allNews = getNews(topic)
		printingNews(topic, allNews)


if __name__ == '__main__':
	main()