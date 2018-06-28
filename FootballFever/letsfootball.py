import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup


def getTeamsName(url):
    absolute_path = 'worldcup/teams/'
    absolute_url = urljoin(url, absolute_path)
    soup = getRequestAndSoup(absolute_url)

    team_details = []
    team_name = []
    team_links = []

    for team in soup.findAll('a', {'class': 'fi-o-media-object__link'}):
        team_links.append(team.get('href'))
    for link in team_links:
        link = urljoin(url, link)
        print(link)
    print(team_links)
    for name in soup.findAll('div', {'class': 'fi-team-card__name'}):
        team_name.append(name.getText().strip())
    for i in range(len(team_links)):
        team_details.append((team_name[i], team_links[i]))

    for i in team_details:
        print(i)


def getRequestAndSoup(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def main():

    url = 'https://www.fifa.com/'
    getTeamsName(url)


if __name__ == '__main__':
    main()
