import threading
import requests

countries = [
    "Germany", "France", "United Kingdom", "Italy", "Spain",
    "Poland", "Netherlands", "Greece", "Portugal", "Sweden",
    "Belgium", "Austria", "Hungary", "Czech Republic", "Ireland"
]

def fetch_universities(country, result):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    if response.status_code == 200:
        universities = response.json()
        result[country] = [univ['name'] for univ in universities]
    else:
        result[country] = []

results = {}

threads = []

for country in countries:
    thread = threading.Thread(target=fetch_universities, args=(country, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for country, universities in results.items():
    print(f"{country}: {universities}")
