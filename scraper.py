import requests
from bs4 import BeautifulSoup
from datetime import datetime

current_date = datetime.now().strftime("%d.%m.%Y")
url = "https://potniski.sz.si/vozni-red/?action=timetables_search&current-language=sl&departure-date=" + current_date + "&entry-station=43203&exit-station=43400"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
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

        formatted_data = f"{departure_station} {departure_time} {travel_time} {arrival_station} {arrival_time}"
        print(formatted_data)
        print('#################################')
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

