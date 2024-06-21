from bs4 import BeautifulSoup

import lxml

soup = BeautifulSoup(open("top10.html", encoding="utf8"), features="lxml")

article = soup.find("article", class_="article-content school-info")

tags = article.find_all("h3")

for tag in tags:
    print(tag.text)
