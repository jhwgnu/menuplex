
# coding: utf-8

# In[18]:

import requests, urllib.request
import requests
from bs4 import BeautifulSoup
# html =urllib.request.urlopen("http://korea.ac.kr/user/restaurantMenuAllList.do?siteId=university&id=university_050402000000")
request = requests.get("http://korea.ac.kr/user/restaurantMenuAllList.do?siteId=university&id=university_050402000000")
html = request.text
soup=BeautifulSoup(html, 'html.parser')

restaurant_list = soup.select('.ku_restaurant ul li')
for restaurant in restaurant_list:
    title = restaurant.findNext('strong').text
    print(title)
    
    ol_tag = restaurant.findNext('ol')
    
    span_tag = ol_tag.findNext('span').findNext('span')
    month = span_tag.contents[1].text
    print(month)
    day = span_tag.contents[3].text
    print(day)
    
    p_tag = span_tag.findNext('p')
    menu = p_tag.text
    print(menu)


# In[ ]:




# In[ ]:



