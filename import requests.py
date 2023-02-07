import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://ikman.lk/en/shops/chanit-flora')

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the specific element you're interested in
element = soup.find('div', {'class': 'example-class'})

# Extract information from the element
info = element.text

# Do something with the information (e.g., send a notification)
print(info)
