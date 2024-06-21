import requests
from bs4 import BeautifulSoup
import pandas as pd

# Đường dẫn đến trang web
url = "https://dienmaythiennamhoa.vn/hang-tieu-dung.html"

# Yêu cầu trang web lấy nội dung
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Tìm tất cả các sản phẩm trên trang web và lưu vào một danh sách
product_list = []
products = soup.find_all("div", attrs={"class": "content-card-cate"})
for product in products:
    name = product.find("h3").text.strip()
    price = product.find("p", attrs={"class": "sale-price product-sale-price"}).text.strip()
    product_list.append([name, price])

# Tạo DataFrame từ danh sách sản phẩm và giá
df = pd.DataFrame(product_list, columns=["Tên sản phẩm", "Giá"])

# In ra DataFrame
print(df)
