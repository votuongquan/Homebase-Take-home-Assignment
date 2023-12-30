import requests
import numpy as np
import pandas as pd
import requests_cache
from bs4 import BeautifulSoup
from selenium import webdriver

requests_cache.install_cache('Task3/real_estate_cache')

data = []
driver = webdriver.Chrome()
div_list = []

# Enter the number of pages you want to crawl
numbers = int(input("Enter the number of pages you want to crawl: "))

for index in range(1,numbers+1):
    url = f"https://batdongsan.com.vn/ban-can-ho-chung-cu-quan-7/p{index}"
    driver = webdriver.Chrome()
    try:
        # Get the web page
        driver.get(url)
        driver.implicitly_wait(10)
        soup = driver.page_source
        source = BeautifulSoup(soup, 'html.parser')
        # Get the list of divs having class js__card
        div_list += source.find_all('div', class_='js__card')
    except Exception as e:
        print('err on web', index)
        continue
    finally:
        # Close the browser window
        driver.quit()

for i in range(len(div_list)):
    # Get the title, price, area, toilet, bedroom, description, publisher
    try:
        try:    
            title = div_list[i].find(class_='pr-title').text.strip()
        except:
            title = div_list[i].find(class_='js__card-title').text.strip()
        price = div_list[i].find(class_='re__card-config-price').text.strip()
        area = div_list[i].find(class_='re__card-config-area').text.strip()
        try:
            toilet = div_list[i].find(class_='re__card-config-toilet').text.strip()
        except:
            toilet = np.nan
        try:
            bedroom = div_list[i].find(class_='re__card-config-bedroom').text.strip()
        except:
            bedroom = np.nan
        try:
            description = div_list[i].find(class_='re__card-description').text.strip()
        except:
            description = np.nan
        try:
            publisher = div_list[i].find(class_='re__card-published-info-agent-profile-name').text.strip()
        except:
            publisher = np.nan
        print({'Title': title, 'Price': price, 'Area': area, 'Toilet': toilet, 'Bedroom': bedroom, 'Description': description, 'Publisher': publisher})
        data.append({'Title': title, 'Price': price, 'Area': area, 'Toilet': toilet, 'Bedroom': bedroom, 'Description': description, 'Publisher': publisher})
    except:
        print("err on", i)
        continue
    
# Save the data to an excel file
df = pd.DataFrame(data)
df.to_excel("Task3/databds.xlsx", index=False)