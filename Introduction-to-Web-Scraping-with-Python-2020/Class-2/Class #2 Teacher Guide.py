from bs4 import BeautifulSoup
import requests
import pandas

page = requests.get('https://nba.com/players')

soup = BeautifulSoup(page.content, 'html.parser')

players = soup.find_all('p', {"class": "nba-player-index__name"})

fnList=[]
lnList=[]
roleList=[]
heightList=[]
weightList=[]

for p  in players:
    #first and last names
    #print(p.contents[0], " ", p.contents[2])
    fnList.append(p.contents[0])
    lnList.append(p.contents[2])
    details = p.next_sibling.find_all("span")
    #print(details[0].text)
    roleList.append(details[0].text)
    info = details[1].find_all("strong")
    #print(info[0].text, "ft", info[1].text, "Inches")
    #print(info[2].text, "lbs")
    heightList.append(info[0].text+"ft"+info[1].text+"Inches")
    weightList.append(info[2].text+"lbs")

extractedData = pandas.DataFrame(
    {"First Name": fnList,
     "Last Name":  lnList,
     "Role": roleList,
     "Height": heightList,
     "Weight": weightList
})
    
extractedData.to_csv('players.csv')
