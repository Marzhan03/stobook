import requests
from bs4 import BeautifulSoup
import re
import random
import psycopg2
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


main_url = "https://astana.blizko.kz/streets"
url="https://karaganda.blizko.kz"
response = requests.get(main_url)

response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
x=1
good_list = soup.find("div", {"class": "list-column"})
all_list=good_list.find("ul",{"class":"streets-list"})
list_href=[]

for l in all_list:
    list_href.append(l.find('a'))
length=len(list_href)
for i in list_href:
    if x % 2 == 0:
        text_massiv=[]
        text=i.text
      
        text=text.strip("\n")
        text_massiv=[text]
        tex_massiv=[2]
       
        conn = psycopg2.connect(dbname='stobook', user='postgres', 
                        password='marzhan', host='localhost')
        cursor = conn.cursor()
        print(text_massiv[0])
        print()
        cursor.execute(f"INSERT INTO book_street (street,city_id) VALUES ('%s', '%s')"%(text_massiv[0],tex_massiv[0]))
        conn.commit()
        cursor.close()
        conn.close()
        
    x=x+1
  
