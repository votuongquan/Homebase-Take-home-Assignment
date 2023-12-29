from bs4 import BeautifulSoup
import requests
import requests_cache
from selenium import webdriver
import pandas as pd

requests_cache.install_cache('Task3/real_estate_cache')

url = f"https://batdongsan.com.vn/ban-can-ho-chung-cu-quan-7/p1" 
data = []
driver = webdriver.Edge()
try:
    driver.get(url)
    driver.implicitly_wait(5)
    soup = driver.page_source
    source = BeautifulSoup(soup, 'html.parser')
    div_elements = source.find_all('div', class_='js__card')
    for i in range(len(div_elements)):
        try:
            title = div_elements[1].find(class_='pr-title').text.strip()
            price = div_elements[i].find(class_='re__card-config-price').text.strip()
            area = div_elements[i].find(class_='re__card-config-area').text.strip()
            toilet = div_elements[i].find(class_='re__card-config-toilet').text
            bedroom = div_elements[i].find(class_='re__card-config-bedroom').text
            description = div_elements[i].find(class_='re__card-description').text.strip()
            publisher = div_elements[i].find(class_='re__card-published-info-agent-profile-name').text.strip()
            location = div_elements[i].find(class_='re__card-location').text.strip()
            data.append({
                'title': title,
                'price': price,
                'area': area,
                'toilet': toilet,
                'bedroom': bedroom,
                'description': description,
                'publisher': publisher,
                'location': location
            })    
        except:
            continue
finally:
    driver.quit()
    print(data)
    
df.to_excel('Task3/data.xlsx', index=False)