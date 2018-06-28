import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup


def getTeamDetails(url, team_url):

    soup = getRequestAndSoup(team_url)

    for a in soup.findAll('div', {'class': 'fi-p'}):
        print('-' * 70)
        if a.find('span', {'class': 'fi-p__num'}):
            print('Jersey No.:', a.find('span', {'class': 'fi-p__num'}).getText())
        else:
            print(':-)')
            break
        if a.find('div', {'class': 'fi-p__info--role'}):
            print('Role:', a.find('div', {'class': 'fi-p__info--role'}).getText().strip())
        if a.find('span', {'class': 'fi-p__info--ageNum'}):
            print('Age:', a.find('span', {'class': 'fi-p__info--ageNum'}).getText())
        for check in a.select('div.fi-p__n a'):
            print('Link to profile:', urljoin(url, check.get('href')))
            print('Full name:', check.get('title').title())

    return


def getTeamsName(url):
    absolute_path = 'worldcup/teams/'
    absolute_url = urljoin(url, absolute_path)
    soup = getRequestAndSoup(absolute_url)

    team_details = []
    team_name = []
    team_links = []

    for team in soup.findAll('a', {'class': 'fi-team-card fi-team-card__team'}):
        team_links.append(urljoin(url, team.get('href')))
    for name in soup.findAll('div', {'class': 'fi-team-card__name'}):
            team_name.append(name.getText().strip())
    for i in range(len(team_links)):
        team_details.append((team_name[i], team_links[i]))

    i = 1
    for team in team_details:
        print('{}'.format(i), team)
        i += 1
    # Detail has been extarcted. Only print statement is left
    while True:
        per = input('Do you want team details (y/n) ')
        if per == 'y':
            team_no = int(input('Enter the team number to get the details of '))
            getTeamDetails(url, team_links[team_no - 1])
            per = 'n'
        else:
            break

    print('I m Back')


def getRequestAndSoup(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def main():

    url = 'https://www.fifa.com/'
    getTeamsName(url)


if __name__ == '__main__':
    main()
