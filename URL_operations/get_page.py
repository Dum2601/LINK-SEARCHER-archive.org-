import requests

r = requests.get('https://archive.org/details/AlamutVladimirBartol') # Site usado para testes


try:
    print('Conexão efetuada com Sucesso!',
          f'{r.url}')
except Exception as err:
    print(f'Erro: {err}')