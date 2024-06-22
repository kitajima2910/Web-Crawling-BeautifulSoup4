from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

# r = urllib.request.urlopen("https://vnexpress.net/").read()
# r = urllib.request.urlopen("https://vietjack.com/van-mau-lop-12/phan-tich-vo-chong-a-phu.jsp").read()
r = urllib.request.urlopen("https://vietjack.com/van-mau-lop-12/top-5-cach-mo-bai-phan-tich-vo-chong-a-phu-hay-nhat.jsp").read()
soup = BeautifulSoup(r, "lxml")
print(soup.prettify()[:100])

# for link in soup.find_all("a"):
#     print(link.text.strip())

file = open("parsed_data.txt", "a", -1, encoding="utf8")

# contents = soup.find_all("div", attrs={"class": "col-md-7 middle-col"})
contents = soup.find_all("p")

for content in contents:
    print(content.text.strip())
    if len(content.text.strip()) > 0:
        file.write(content.text.strip() + "\n")
file.flush()
file.close()
