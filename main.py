#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

# thread to check
url = "https://secure.runescape.com/m=forum/forums?290,291,thd,908,66254470"

# thread title we care about
clan_str = "-~-~-~-~ DARK DREAMS ~-~-~-~-"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# find all thread titles on the current page
thread_titles = soup.find_all('h3')

# strip the tags
clans = []
for thread in thread_titles:
    clans.append(thread.get_text())

# check if the clan is on the list
try:
    pos = clans.index(clan_str)
    if pos != 0:
        print("We're currently {} on the recruitment forum. Time for a bump?".format(pos))
    else:
        print("We're #1, we're #1!")
except:
    print("We're not on the front page, definitely time for a bump.")

# print a ranking
print("-----")
p = 1
for clan in clans:
    print("#{}: {}".format(p,clan))
    p += 1
