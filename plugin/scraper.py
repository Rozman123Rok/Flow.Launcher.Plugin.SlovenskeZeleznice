from flowlauncher import FlowLauncher
import webbrowser
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

class Scraper(FlowLauncher):

    current_date = datetime.now().strftime("%d.%m.%Y")
    URL1 = "https://potniski.sz.si/vozni-red/?action=timetables_search&current-language=sl&departure-date=" + current_date + "&entry-station=43203&exit-station=43400"
    URL2 = "https://potniski.sz.si/vozni-red/?action=timetables_search&current-language=sl&departure-date=" + current_date + "&entry-station=43400&exit-station=43203"

    GITHUB_URL = "https://github.com/Rozman123Rok/Flow.Launcher.Plugin.SlovenskeZeleznice"
    GITHUB_USAGE = "https://github.com/Rozman123Rok/Flow.Launcher.Plugin.SlovenskeZeleznice?tab=readme-ov-file#usage"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    query_results = []
    ICON_PATH = "Images\\logo.jpg"
    session = requests.Session()

    def add_message(self, text: str, subtext: str = None, url: str = None):
        self.query_results.append({
            "Title": text,
            "SubTitle": subtext,
            "IcoPath": self.ICON_PATH,
            "JsonRPCAction": {
                "method": "open_url",
                "parameters": [url or self.GITHUB_URL]
            }
        })

    def query(self, query):
        if query == "1": 
            # Poljcane -> Maribor
            self.get_data(self.URL1)
        elif query == "2" or query == "":
            # Maribor -> Poljcane
            self.get_data(self.URL2)
        else:
            self.add_message("Query not defined, check GitHub page for info", query, self.GITHUB_USAGE)

        return self.query_results 
    
    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

    def get_data(self, url):
        response = requests.get(url, headers = self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            connections = soup.find_all('div', class_='connection card no-shadow connection-active')

            for connection in connections:
                departure_station = connection.select_one('.col-12 strong').get_text(strip=True)

                departure_time = connection.select_one('.col-12 strong:nth-of-type(2)').get_text(strip=True)

                travel_time = connection.select_one('.row.item:nth-of-type(3) strong').get_text(strip=True)

                arrival_station_elem = connection.select_one('.row.item:nth-of-type(4) .row .col-12')
                arrival_info = arrival_station_elem.get_text().split(' ')
                arrival_station = arrival_info[2]
                arrival_time = arrival_info[4]

                self.add_message(departure_station + " : " + departure_time + " -> " + arrival_station + " : "+ arrival_time, '', url)
        else:
            self.add_message('Error', str(response.status_code), url)
