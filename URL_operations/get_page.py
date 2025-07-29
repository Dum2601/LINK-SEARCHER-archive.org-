import requests
from bs4 import BeautifulSoup

class Page:
    def __init__(self, link):
        self.link = link 
        self.request = None  

    def check_page(self): # See if the code can reach the page
        try:
            self.request = requests.get(self.link, timeout=5)  # try acess
            self.request.raise_for_status()  # check status
            print(f'Page acess OK: {self.request.status_code}')
            self.soup = BeautifulSoup(self.request.text, 'html.parser')
            return True
        except requests.exceptions.RequestException as err:
            print('Error:',
                  f'\n{err}')
            return False      

    def search_download_methods(self): # Show the downloads avaible in archive
        download_section = self.soup.find("section", class_="boxy item-download-options")

        if download_section:
            links = download_section.find_all("a", class_="format-summary download-pill")

            # Take the download itens
            hrefs = []
            for link in links:
                href = "https://archive.org" + link["href"]
                hrefs.append(href)

            return hrefs
        else:
            print("Download Section not found.")
            return None  # Grant that somethings is returned

    def download_link(self):
        if self.check_page():
            return self.search_download_methods() 
        elif self.check_page() == False:
            print(f"Couldn't reach the download methods")
            return None


