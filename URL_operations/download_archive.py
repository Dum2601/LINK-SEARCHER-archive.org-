# import requests
# import os
# import re


# def there_is_a_torrent(html_content):
#     try:
#         # Procurar por um link que termina em ".torrent"
#         match = re.search(r'href="(/download/[^"]+\.torrent)"', html_content)
#         if match:
#             torrent_path = match.group(1)
#             full_torrent_url = 'https://archive.org' + torrent_path
#             print(f'Encontrado torrent: {full_torrent_url}')
#             return full_torrent_url
#         else:
#             print('Nenhum link de torrent encontrado.')
#             return None
#     except Exception as err:
#         print('Erro encontrado:', err)
#         return None

# def download_torrent(torrent_url, file_name='arquivo.torrent'):
#     try:
#         os.system(f'curl -L -o "{file_name}" "{torrent_url}"') # Comando para baixar no terminal
#         print(f'Torrent baixado como {file_name}')
#     except Exception as err:
#         print('Erro ao baixar:', err)

# # Main
# try:
#     page_url = 'https://archive.org/details/AlamutVladimirBartol'
#     r = requests.get(page_url)
    
#     torrent_link = there_is_a_torrent(r.text)
    
#     if torrent_link:
#         download_torrent(torrent_link, 'AlamutVladimirBartol.torrent')
#     else:
#         print('Nenhum torrent para baixar.')
# except Exception as err:
#     print('Erro geral:', err)
