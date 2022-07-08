#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def alert(trigger="always", threshold=3,pos=False):
    """triggers
    not_on_front - Send a notification if we're not on the first page
    threshold - Send a notification if we're ranked higher than X
    always - Send a notification no matter what
    """
    if trigger == "not_on_front":
        if pos == False:
            notify("We're not on the front page anymore!")

    if trigger == "threshold":
        if pos == False:
            notify("We're not on the front page anymore!")
        elif pos > threshold:
            notify("We're no longer in the top {}!".format(threshold)) 

    if trigger == "always":
        if pos == False:
            notify("We're not on the front page anymore!")
        elif pos != 1:
            print("We're currently {} on the recruitment forum. Time for a bump?".format(pos+1))
        else:
            print("We're #1, we're #1!")


def notify(s):
    print(s)

def rank(clans):
    p = 1
    for clan in clans:
        print("#{}: {}".format(p,clan))
        p += 1

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

pos = False
try:
    pos = clans.index(clan_str) + 1
except:
    pass

alert(trigger="threshold", threshold=3,pos=pos)