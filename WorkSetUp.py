import webbrowser as web
import os

def workAuto():
    # open an application in my system eg vscode
    # codePath = "C:/Users/Techfaith/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    # os.startfile(codePath)
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # URLS = ('go54.com', 'cursor.com', 'freemiumtech.com')
    # for url in URLS:
    url = input("Enter the url you want to open: ")
    web.get(chrome_path).open(url)

workAuto()