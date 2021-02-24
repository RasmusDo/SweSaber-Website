import requests
from bs4 import BeautifulSoup

urls = ["https://scoresaber.com/global?country=se", "https://scoresaber.com/global/2&country=se"]

playerNames = {}

for i in urls:

    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'lxml')

    player = soup.find_all("span", {"class": "songTop pp"})
    playerPP = soup.find_all("span", {"class": "scoreTop ppValue"})

    for idx, key in enumerate(player):
        for i in playerPP[idx]: 
            playerPP[idx] = i
        for i in player[idx]:
            player[idx] = i

        playerNames[player[idx]] = playerPP[idx]

with open("database.csv", "w", encoding="utf8") as f:
    for i in playerNames:
        f.write(f"{i}\n{playerNames[i]}\n\n")