import sys
import requests
from bs4 import BeautifulSoup
import notify2 as noti
from time import sleep

def message(msg):
	ICON_PATH="/home/shivg/cricket.png"
	m = msg.split('|')
	noti.init("Cricket Notification")
	noti.Notification('Live Score', m[0], icon = ICON_PATH).show()
	return

def main():
	url = "http://static.cricinfo.com/rss/livescores.xml"	
	try:
		r = requests.get(url)
	except requests.exceptions.RequestException as e:
		print('No internet connection')
		sys.exit(1)
	soup = BeautifulSoup(r.text, 'lxml')
	
	guidLinks = [link.find('guid').text for link in soup.findAll('item')]

	for link in guidLinks:
		s = requests.get(link)
		soup = BeautifulSoup(s.text, 'lxml')
		score = soup.findAll('title')
		message(score[0].text)

		sleep(3)

if __name__ == '__main__':
	main()