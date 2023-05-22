import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg

# define a function to extract the link from a given URL
def extract_link_from_url(url):
    # send a GET request to the URL
    response = requests.get(url)

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # find the desired element using CSS selectors
    link_element = soup.select_one("#leaderboard div.posts.post_single:last-child center:nth-child(3) div.downLink:first-child a")

    # extract the link from the element
    if link_element:
        link = link_element.get('href')
        return link
    else:
        return None

# define the PySimpleGUI layout
layout = [
    [sg.Text("Enter the URLs to scrape, one per line:")],
    [sg.Multiline(size=(60, 10), key="url_input")],
    [sg.Button("Extract Links")],
    [sg.Output(size=(60, 20))]
]

# create the PySimpleGUI window
window = sg.Window("URL Scraper", layout)

# event loop to process GUI events
while True:
    event, values = window.read()

    # close the window if the user clicks the X button or presses the Esc key
    if event == sg.WINDOW_CLOSED or event == "Exit" or event == "Escape:":
        break

    # extract the links if the user clicks the "Extract Links" button
    if event == "Extract Links":
        urls = [url.strip() for url in values["url_input"].split("\n")]

        for url in urls:
            link = extract_link_from_url(url)
            if link:
                print(link)
            else:
                print("Element not found in", url)

# close the PySimpleGUI window
window.close()
