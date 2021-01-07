#!/usr/bin/env python3

"""There has been a lot of activity with astronauts going up and down due to SpaceX! There is a public API that records all current people in space and what vessel they are on. Check it out at http://api.open-notify.org/astros.json

Your challenge this morning is to do the following:

Access the API from the link above, pull/translate the JSON!

This API changes EVERY SINGLE TIME astronauts leave/arrive in space! Write a script that would give the following output:

People in space: 3
Chris Cassidy on the ISS
Anatoly Ivanishin on the ISS
Ivan Vagner on the ISS
BONUS- You should be able to run this exact same script a year from now and that inevitably updated list of astronauts would still display correctly! How? That's the challenge!

"""

import requests
astros = requests.get('http://api.open-notify.org/astros.json').json()
print("People in space: ", astros["number"])
for astronauts in astros["people"]:
    print(f"{astronauts['name']} on the {astronauts['craft']}")
