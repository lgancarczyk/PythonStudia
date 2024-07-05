import xml.etree.ElementTree as ET
import requests

def fetch_and_parse_xml(url):
    response = requests.get(url)
    response.raise_for_status()
    return ET.fromstring(response.content)

def extract_cd_data(root):
    cd_list = []
    for cd in root.findall('CD'):
        artist = cd.find('ARTIST').text
        title = cd.find('TITLE').text
        cd_list.append((artist, title))
    return cd_list

def main():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    root = fetch_and_parse_xml(url)
    cd_list = extract_cd_data(root)
    
    for artist, title in cd_list:
        print(f"({artist}, {title})")

if __name__ == "__main__":
    main()
