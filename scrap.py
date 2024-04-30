import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the page containing the hero images
url = "https://dota2.gamepedia.com/Heroes"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the specified HTML tag and class
    hero_elements = soup.find_all('td', class_='heroentry')

    # Create a directory to save the images
    os.makedirs("hero_images", exist_ok=True)

    # Loop through each hero element
    for hero in hero_elements:
        # Extract the hero name and image URL
        hero_name = hero.find('span', class_='tooltiplink').text.strip()
        img_url = hero.find('img')['src']

        # Download the image and save it to the directory
        img_data = requests.get(img_url).content
        with open(f"hero_images/{hero_name}.png", 'wb') as handler:
            handler.write(img_data)
            
        print(f"Downloaded: {hero_name}")

    print("All hero images downloaded successfully!")
else:
    print("Failed to fetch the webpage.")