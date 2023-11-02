import requests
from bs4 import BeautifulSoup


# url = "https://example.com" // The url to scrape
url = "https://ski.bde42.fr/"
response = requests.get(url)

if response.status_code == 200:  # if the URL exist
    html = response.text
else:
    print("Error while loading this page.")

soup = BeautifulSoup(html, 'html.parser')

# Print in terminal:
# links = []
# for link in soup.findAll('a'):
#     links.append(link.get('href'))
# print(links)

# Print in Output file:
output_file = open('extract.txt', 'w', encoding='utf-8')
for link in soup.findAll('a'):
    output_file.write(link.get('href') + '\n')
output_file.close()
