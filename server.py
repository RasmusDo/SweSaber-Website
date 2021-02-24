from flask import Flask, render_template
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/server.py")
def click():
    urls = ["https://scoresaber.com/global?country=se", "https://scoresaber.com/global/2&country=se"]

    playerNames = {}

    for i in urls:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, 'lxml')

        player = soup.find_all("span", {"class": "songTop pp"})
        playerPP = soup.find_all("span", {"class": "scoreTop ppValue"})

        for idx in range(len(player)):
            for i in playerPP[idx]: 
                playerPP[idx] = i
            for i in player[idx]:
                player[idx] = i

            playerNames[player[idx]] = playerPP[idx]
    return playerNames

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
