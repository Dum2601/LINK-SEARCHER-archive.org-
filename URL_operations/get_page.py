import requests

class Page:
    def __init__(self, link):
        self.link = link 
        self.request = None  

    def check_page(self):
        try:
            self.request = requests.get(self.link, timeout=5)  # try acess
            self.request.raise_for_status()  # check status
            print(f'Page acess OK: {self.request.status_code}')
            return True
        except requests.exceptions.RequestException as err:
            print('Error:',
                  f'\n{err}')
            return False
            
            
        
    def fixing_link(self):
        if self.check_page() == True:
            self.search_download_methods(self) # Makes sure that the correct function is called (second verifing)
            print('Was necessary verify twice in fixing_link() to go to correct function (search_download_methods())') # To know the function was not called in correct place

        elif self.check_page() == False:
            print("The program couldn't find the page writed, can you try once more with the correct link?")
            
            


    def search_download_methods(self):
        # Verifica as opções de download após a checagem
        print('Agora sim')

    @property
    def download_link(self):
        


# Checa no check page, se der True, chamar a de procurar downloads, se der errado, chamar a que concerta o link


# page = Page('https://archive.org/details/AlamutVladimirBartol')
# page = Page('https://archive.org/details/AlamutVladim')

if page.check_page() == True:
    print('Deu fora da função')
else:
    print('Deu o erro certo')