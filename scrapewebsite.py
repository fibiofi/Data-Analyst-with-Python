import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    

    products = soup.find_all('h3')
    

    for product in products:
        title = product.a['title']
        price = product.find_next('p', class_='price_color').text
        print(f"Judul: {title}, Harga: {price}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
