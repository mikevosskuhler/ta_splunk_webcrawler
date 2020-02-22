from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from check_stock import check_inventory
import sys
producturl = str(sys.argv[1])
basketurl = str(sys.argv[2])

html = check_inventory(producturl, basketurl)

soup = BeautifulSoup(html, 'html.parser')

inventory_count = soup.find_all('select', class_="js_quantity_dropdown tst_item_count_selection")[0].contents[21].contents

print(inventory_count)

producturl = "https://www.bol.com/nl/p/philips-sonicare-diamondclean-hx9363-63-elektrische-tandenborstel-roze/9200000073453746/?bltgh=v7YkkGxLDCLFb2OmUblFMw.1_30.34.ProductImage"
basketurl = "https://www.bol.com/nl/order/basket.html"
