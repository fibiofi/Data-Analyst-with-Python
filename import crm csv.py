import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('h3')

    # Inisialisasi list untuk menyimpan data
    titles = []
    prices = []

    for product in products:
        title = product.a['title']
        price = product.find_next('p', class_='price_color').text

        # Menambahkan data ke list
        titles.append(title)
        prices.append(price)

    # Membuat DataFrame menggunakan pandas
    data = {'Judul': titles, 'Harga': prices}
    df = pd.DataFrame(data)

    # Menyimpan DataFrame ke file Excel
    df.to_excel('toscrape.xlsx', index=False)

    print("Data berhasil disimpan ke toscrape.xlsx")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
