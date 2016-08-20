# -*- coding: utf-8 -*-
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://scrapebook22.appspot.com"

response = urlopen(url).read()

soup = BeautifulSoup(response)

print soup.html.head.title.string

csv_file = open("email.csv", "w")

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = url + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"}).string
        name = person_soup.findAll("h1")[1].string
        city = person_soup.find("span", attrs={"data-city": True}).string
        csv_file.write(name + "," + email + "," + city + "\n")


csv_file.close()