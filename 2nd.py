import requests
from bs4 import BeautifulSoup

# Define a function to extract the link from a given URL
def extract_link_from_url(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the desired element using CSS selectors
    link_element = soup.select_one("#leaderboard div.posts.post_single:last-child center:nth-child(3) div.downLink:first-child a")

    # Extract the link from the element
    if link_element:
        link = link_element.get('href')
        return link
    else:
        return None

# Read URLs from input file
with open('links.txt', 'r') as file:
    urls = file.read().splitlines()

# Extract links and save them to output file
with open('output.txt', 'w') as file:
    for url in urls:
        link = extract_link_from_url(url)
        if link:
            file.write(link + '\n')
        else:
            file.write(f'Element not found in {url}\n')
