import requests
import inspect
from bs4 import BeautifulSoup

class Page:
    def __init__(self, link):
        self.link = link 
        self.request = None  

    def check_page(self):
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

    def search_download_methods(self):
        download_section = self.soup.find("section", class_="boxy item-download-options")

        if download_section:
            links = download_section.find_all("a", class_="format-summary download-pill")

            # Take the download itens
            hrefs = ["https://archive.org" + link["href"] for link in links]

            return hrefs  
        else:
            print("Download Section not found.")
            return None  # Grant that somethings is returned

    def download_link(self):
        if self.check_page():
            return self.search_download_methods()  # Está chamando o search_download_methods()
        elif self.check_page() == False:
            return f'Deu errado na função {inspect.currentframe().f_code.co_name}() da classe {self.__class__.__name__}'

# Teste:
page = Page('https://archive.org/details/AlamutVladimirBartol').download_link()
print(page)
