import requests
from bs4 import BeautifulSoup
import time

# URL dan cookie token
url = "https://v2-students.unpad.ac.id/academic/thesis#taRepository"
cookie = {"token": "J0ke880SwgYRrJGXferI9sQmhTz4UawmeDX91tPm"}

# Akses website dengan cookie token
response = requests.get(url, cookies=cookie)

# Buat objek BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Isi form search
search_input = soup.find('input', {'xpath': "/html/body/div/div/div/div/div[2]/div[2]/section/main/div[2]/div[2]/section/div[1]/form/input"})
search_input['value'] = "rancang bangun"

# Klik button
button = soup.find('button', {'xpath': "/html/body/div/div/div/div/div[2]/div[2]/section/main/div[2]/div[2]/section/div[1]/button"})
response = requests.post(url, cookies=cookie, data=button.attrs['value'])

# Tunggu 5 detik
time.sleep(5)

# Ambil teks
result_text = soup.find('span', {'xpath': "/html/body/div/div/div/div/div[2]/div[2]/section/main/div[2]/div[2]/section/div[2]/div[1]/div/div[3]/span[2]"}).text

print(result_text)
