**English** # Portuguese below
About this project
Recently, I often had to download some files from archive.org and decided to put my recent studies into practice: I created a small script to make my task easier by generating the download links directly for the terminal.

However, I decided to keep it open and free! I would be honored if you wish to contribute—feel free to submit Pull Requests or fork it.
Just keep one thing in mind: this is a collaborative code that can be used however you like, but it will remain free software under the GNU GPL v3 license.

About the GNU GPL v3 License
The GNU General Public License v3 (GPLv3) is a free software license that guarantees:

Freedom to use, modify, and share the software.

Any distributed modified version must also be licensed under GPLv3.

To learn more, please read the official documentation:
https://www.gnu.org/licenses/gpl-3.0.en.html

How to use
Requirements:

Python 3

Libraries: requests and beautifulsoup4

Running the project:

Access via terminal:

bash
Copiar
Editar
python3 main.py
If you face any issues on Windows, you may also run it using the main.bat file.

Want to contribute?
Planned improvements include:

Changes in the Page class

Check the HTTP status code directly instead of relying on raise_status (see original documentation).

Add this validation to each method inside the Page class.

Add a Front-End:

Remove the current terminal dependency in the future (maybe...).

Feel free to open issues or submit pull requests!

---

(Português)
Sobre este projeto
Ultimamente, tenho precisado baixar alguns arquivos do archive.org e decidi pôr em prática meus estudos recentes: criei um pequeno script para facilitar minha tarefa, gerando os links de download diretamente no terminal.

Porém, decidi deixá-lo aberto e livre! Ficaria lisonjeado caso queira contribuir—sinta-se à vontade para enviar Pull Requests ou fazer forks.
Só tenha uma coisa em mente: este é um código colaborativo que pode ser usado como desejar, mas ele continuará sendo software livre sob a licença GNU GPL v3.

Sobre a licença GNU GPL v3
A GNU General Public License v3 (GPLv3) é uma licença de software livre que garante:

Liberdade para usar, modificar e compartilhar o software.

Qualquer versão modificada distribuída também deve estar sob a GPLv3.

Para saber mais, leia a documentação oficial:
https://www.gnu.org/licenses/gpl-3.0.pt-br.html

Como usar
Requisitos:

Python 3

Bibliotecas: requests e beautifulsoup4

Executando o projeto:

Acesse pelo terminal:

bash
Copiar
Editar
python3 main.py
Caso enfrente dificuldades no Windows, também é possível executar o arquivo main.bat.

Deseja contribuir?
As próximas atualizações planejadas são:

Alterações na Class Page

Checar o status HTTP diretamente em vez de usar o raise_status (ver a documentação original).

Adicionar essa verificação em cada método da classe Page.

Adicionar um Front-End:

Remover a dependência atual de ser apenas via terminal (no futuro, talvez...).

Sinta-se livre para abrir issues ou enviar pull requests!

