const Http = new XMLHttpRequest();
const url='https://new.scoresaber.com/api/players/76561198356628789/full';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
    var response = JSON.parse(Http.responseText)

    informationElement = document.getElementById("information")
    informationElement.innerHTML = response["playerInfo"]["pp"] + " " + response["playerInfo"]["playerName"]
}
