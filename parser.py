import requests
from bs4 import BeautifulSoup
import re
import random

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


main_url = "https://www.flip.kz"
genreurl="https://www.flip.kz/catalog?subsection=1"
genre_massiv=[]
genre_href_massiv=[]
response = requests.get(genreurl)

response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

good_list = soup.find("div", {"id": "content"})
all_genre = good_list.find_all("div", {"class": "title_m"})
all_pages_massiv=[]
base=[]
i=0

import psycopg2



for genre in all_genre:
    #print(genre.text)
    genre_massiv.append(genre.text)
    genre_href = genre.find('a', {'class': "title"})

    response_each_genre_page = requests.get(main_url + genre_href['href'])

    genre_href_massiv.append(main_url+genre_href['href'])
    genre_href=main_url+genre_href['href']






    #print("sdasdsd", genre_massiv[i])
    pageurl = genre_href

    response = requests.get(pageurl)
    response_text = response.text
    soup = BeautifulSoup(response_text, "html.parser")
    good_list = soup.find("div", {"id": "content"})
    page_table = good_list.find("table", {"class": "pages"})

    all_pages = page_table.find_all("a", {"style": "font-weight:normal"})

    all_pages_href_massiv = []
    for page in all_pages:
        # print(genre.text)
        page_href = main_url+"/"+page['href']
        all_pages_href_massiv.append(page_href)

    i=i+1
    caturl = genre_href

    all_pages_href_massiv.insert(0,genre_href)
    if len(all_pages_href_massiv)>1:
        all_pages_href_massiv =all_pages_href_massiv[0:1]

    for pages in all_pages_href_massiv:

        response = requests.get(pages)
        response_text = response.text
        soup = BeautifulSoup(response_text, "html.parser")


        good_list = soup.find("div", {"class": "good-list"})
        all_books = good_list.find_all("div", {"class": "placeholder"})

        # print(len(all_books))
        for book in all_books:
            book_href = book.find('a', {'class': "pic l-h-250"})
            # print("jjhk",book_href)
            response_each_book_page = requests.get(main_url + book_href['href'])


            each_book_soup = BeautifulSoup(response_each_book_page.text, "html.parser")
            each_book_content = each_book_soup.find("div", {'id': 'content'})

            book_table = each_book_content.find("table", {'id': 'prod'})
            tr = book_table.find("tr")
            name = tr.find("h1").text
            name_massiv=[name]
            price = each_book_soup.find("meta", {'itemprop': 'price'})
            print(name)

            description = each_book_soup.find("span", {'itemprop': 'description'})
            CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            description = cleanhtml(description.text)
            description_massiv=[description]

            img_book=each_book_soup.find("div",{"class":"product_img_cell"})
            img=img_book.find("img")
            img_url=img['src']
            img_url="https:"+img_url
            img_url_massiv=[img_url]

            publishing=each_book_soup.find("div",{"style":"padding:10px"})
            publishing = publishing.find("p", {"style": "width:90%;margin-bottom:5px"}).find("b").text
            conn = psycopg2.connect(dbname='stobook', user='postgres', 
                        password='marzhan', host='localhost')
            cursor = conn.cursor()

          
            page = random.randint(200, 600)
            page_massiv=page
            cost = random.randint(2000, 6000)
            cost_massiv = cost
            author = tr.find_all("td")[1].find("p").text
            author_massiv=[author]

            print(genre.text)
            genre_massiv=[genre.text]

            publishing_massiv=[publishing]
            print("DDDDDDDD:", author_massiv[0])
            cursor.execute("SELECT * FROM book_author WHERE name='%s'"%author_massiv[0])

            result_author=cursor.fetchall()
            if len(result_author) >0:
                print("gbg")
            else:
                cursor.execute(f"INSERT INTO book_author (name) VALUES ('%s')"%author_massiv[0])



            cursor.execute("SELECT * FROM book_publishing  WHERE name='%s'"%publishing_massiv[0])
            result_publishing = cursor.fetchall()

            if len(result_publishing) > 0:
                print("gbg")
            else:
                cursor.execute(f"INSERT INTO book_publishing (name) VALUES ('%s')"%publishing_massiv[0])

            cursor.execute("SELECT * FROM book_genre  WHERE genrename='%s'"%genre_massiv[0])
            result_genre = cursor.fetchall()
            if len(result_genre) > 0:
                print("gbg")
            else:
                cursor.execute(f"INSERT INTO book_genre (genrename) VALUES ('%s')"%genre_massiv[0])

            cursor.execute("SELECT id FROM book_author  WHERE name='%s'"%author_massiv[0])
            id_author = cursor.fetchone()
            id_author=id_author[0]
            cursor.execute("SELECT id FROM book_publishing  WHERE name='%s'"%publishing_massiv[0])
            id_publishing = cursor.fetchone()
            id_publishing=id_publishing[0]

            cursor.execute("SELECT id FROM book_genre  WHERE genrename='%s'"%genre_massiv[0])
            id_genre=cursor.fetchone()
            id_genre=id_genre[0]

            books_massiv = (name, img_url, page, description,id_author,id_publishing,id_genre,cost)
            id_massiv=(id_author,id_publishing,id_genre)
            cursor.execute(f"INSERT INTO book_book (bookname,bookimg,number_of_pages,description,author_id,publishing_id,genre_id,cost) VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s')"%(books_massiv[0],books_massiv[1],books_massiv[2],books_massiv[3],books_massiv[4],books_massiv[5],books_massiv[6],books_massiv[7]))
             #   f"INSERT INTO book_book (bookname,bookimg,number_of_pages,description)  VALUES (?,?,?,?)",books_massiv)
            #cursor.execute(
             #   f"INSERT INTO book_book (author_id,publishing_id,genre_id)  VALUES (?,?,?)",id_massiv)
            conn.commit()
            cursor.close()
            conn.close()

print(base)

