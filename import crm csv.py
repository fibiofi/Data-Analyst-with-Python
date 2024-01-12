import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/catalogue/page-1.html'
titles = []
prices = []
stock = []

#looping 1001 data
for page_num in range(1, 51):  # Ubah angka 51 sesuai dengan jumlah halaman
    page_url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_containers = soup.find_all('article', class_='product_pod')

        for container in product_containers:
            product_type = container.h3.a['title']

            stock_elem = container.find('p', class_='instock availability')
            stock_value = stock_elem.text.strip() if stock_elem else 'Tidak ditemukan'

            price_elem = container.find('p', class_='price_color')
            price = price_elem.text.strip() if price_elem else 'Tidak ditemukan'

            # Menambahkan data ke list
            titles.append(product_type)
            stock.append(stock_value)
            prices.append(price)

        print(f"Data dari halaman {page_num} berhasil diambil.")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        break  # Berhenti jika gagal mengambil halaman

# Membuat DataFrame menggunakan pandas
data = {'Judul': titles, 'Stok': stock, 'Harga': prices}
df = pd.DataFrame(data)

# Menyimpan DataFrame ke file Excel
df.to_excel('analisisprofperusahaan.xlsx', index=False)

print(f"Data berhasil disimpan ke analisisprofperusahaan.xlsx (Jumlah data: {len(titles)})")
