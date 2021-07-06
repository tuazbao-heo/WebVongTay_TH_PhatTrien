class configs:
    target_url = 'https://www.shein.com.vn/'
    target_bracelets_url = 'https://www.shein.com.vn/Bracelets-c-1758.html'

# import librarie
from sys import prefix
from bs4 import BeautifulSoup
import requests as req
import random

# retrival soup on bracelets-web site from configs.target_bracelets url
response = req.get(configs.target_bracelets_url)
htmlBraceletsWeb = response.text

# the valuable tags
soup = BeautifulSoup(htmlBraceletsWeb, 'html.parser')
product_item_wrappers = soup.find_all("div", {"class": 'S-product-item__wrapper'}, limit= 100)

# product mapping
products = {}
product_index = 1 #auto_increment default start at 1

# extract soup to products
for wrapper in product_item_wrappers:
    #tag_anchor = wrapper.find('a')
    tag_img = wrapper.find('img')
    
    # declare product field values
    bracelet_name = tag_img.get('alt')
    bracelet_image_src_url = tag_img.get('data-src')
    bracelet_price = (random.randint(7, 50))*10000
    bracelet_in_stock = (random.randint(10, 50))

    # declare a product: dict
    product = {}
    product['name'] = bracelet_name
    product['image_url'] = bracelet_image_src_url
    product['price'] = bracelet_price
    product['in_stock'] = bracelet_in_stock

    # map product into products
    index = str(product_index)
    products[index] = product

    # increase product index
    product_index += 1

# queries insert data into SAN_PHAM
for key in products.keys():
    query = f"insert into SAN_PHAM(TEN, GIA, SO_LUONG_CON, SO_LUONG_DA_BAN) " + \
            f"values ('{products[key]['name']}', {products[key]['price']}, {products[key]['in_stock']}, 0);"
    print(query)

# queries insert data into HINH_ANH
for key in products.keys():
    image_url = products[key]['image_url']
    query = f"insert into HINH_ANH(URL) values('{image_url}');"
    print(query)

# queries insert data into SAN_PHAM_HINH_ANH
for key in products.keys():
    query = f"insert into SAN_PHAM_HINH_ANH(MA_SAN_PHAM, MA_HINH_ANH, MOTA) values" + \
            f"({key}, {key}, '{products[key]['name']}');"
    print(query)




