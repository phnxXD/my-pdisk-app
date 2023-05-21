import PySimpleGUI as sg
import requests

def list_folder_files(api_url, folder_id, api_key):
    url = f"{api_url}/api/folder/list?fld_id={folder_id}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        files = data["result"]["files"]
        file_links = [file["link"] for file in files]
        return file_links
    else:
        sg.popup(f"Failed to list folder files. Status code: {response.status_code}")

# GUI layout
layout = [
    [sg.Text("API URL"), sg.Input(key="-API_URL-", default_text="https://pdisk.pro")],
    [sg.Text("Folder ID"), sg.Input(key="-FOLDER_ID-", default_text="0")],
    [sg.Text("API Key"), sg.Input(key="-API_KEY-", default_text="12286gxnvnjoj0jd12f8t")],
    [sg.Button("List Files"), sg.Button("Exit")],
    [sg.Multiline(size=(60, 20), key="-LINKS-", disabled=True)]
]

# Create the window
window = sg.Window("Folder File Links", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "List Files":
        api_url = values["-API_URL-"]
        folder_id = values["-FOLDER_ID-"]
        api_key = values["-API_KEY-"]
        
        file_links = list_folder_files(api_url, folder_id, api_key)

        # Display file links in the output area
        window["-LINKS-"].update("\n".join(file_links))

# Close the window
window.close()
