# if you want to scrap a website:
# 1.use the API
# 2.HTML Web Scraper using some tool like beautifull 4

# step-0 Install all the requirment
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
#step 1 get the html
r = requests.get(url)
htmlContent=r.content
# print(htmlContent)
#step 2 parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
# step 3 html tree traversal
# Commonly used types of objectd
# print(type(title))# 1. Tag
# print(type(title.string))# 2. Navigable string
# print(type(soup))   # 3.BeautyfullSoup
# 4.Comment
markup = "<p><!-- this is comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


# Get the title of the HTMl page
title=soup.title

#get all the paragraphfrom the page
paras = soup.find_all('p')
print(paras)

#get all the achor tag from the page
anchors = soup.find_all('a')
all_links=set()
#get all the links in achour tag
for link in anchors:
    if(link.get('href') !='#'):
        linkText="https://codewithharry.com" +link.get('href')
        all_links.add(linkText)
        print(linkText)
print('anchors')

# get classes of any element in the html
print(soup.find('p')['class']) 

# find all the elements with class lead/
print(soup.find_all('p',class_="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# navbarSupportedContent = soup.find(id="navbarSupportedContent")
# for elem in navbarSupportedContent.children:
#     print(elem)







