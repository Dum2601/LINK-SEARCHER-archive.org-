Finalizar o algoritmo e deixar ele público.
Ele vai baixar o arquivo do URL que eu colocar do site https://archive.org/
O seguinte livro está sendo usado para testes https://archive.org/details/AlamutVladimirBartol

Até o momento, testei apenas o download com o torrent que está ok.
Basicamente ele manda uma requisição para ver se está com o arquivo e depois, com um GET, pega o link do download.
O algoritmo consiste em pegar o link para o download, usar a biblioteca OS para rodar o script para baixar esse link direto pelo CMD e direcionar para a pasta desejada.

TO-DO:

-> Refazer toda a página das funções que baixam, teve ajuda do GPT para testes, quero tudo sozinho agora que sei que funciona.
-> Colocar um README de respeito e bilíngue.
-> Revisar a licensa.
-> Postar e dizer que é código aberto para contribuições.
-> No futuro, pensar em um front-end por uma biblioteca simples do python.
