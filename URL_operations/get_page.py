import requests
import inspect

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


    def search_download_methods(self):
        # Verifica as opções de download após a checagem
        pass

    def download_link(self):
        # check conection status:
        ## Testando, o que tiver de ocorrer ficar no que está certo, o que der errado ir para o False
        if self.check_page():
            return 'Deu certo' # TO-DO: Continuar as operações aqui
        elif self.check_page() == False:
            return f'Deu errado na função {inspect.currentframe().f_code.co_name}() da classe {self.__class__.__name__}' # TO-DO: Pedir para ele colocar o link correto

        


# Checa no check page, se der True, chamar a de procurar downloads, se der errado, chamar a que concerta o link


page = Page('https://archive.org/details/AlamutVladimirBartol').download_link()
# page = Page('https://archive.org/details/AlamutVladim').download_link()


print(page)