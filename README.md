## **English**

### Portuguese below

## About this project

Recently, I often had to download some files from [archive.org](https://archive.org) and decided to put my recent studies into practice: I created a small script to make my task easier by generating the download links directly in the terminal.

The usage is simple: **just paste the link to the item page from the [archive.org](https://archive.org) website that you want to download**.

However, I decided to keep it open and free! I would be honored if you wish to contribute—feel free to submit Pull Requests or fork it.
Just keep one thing in mind: this is a collaborative code that can be used however you like, but it will remain free software under the GNU GPL v3 license.

### About the GNU GPL v3 License

The GNU General Public License v3 (GPLv3) is a free software license that guarantees:

* Freedom to use, modify, and share the software.
* Any distributed modified version must also be licensed under GPLv3.

To learn more, please read the official documentation:
[https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)

### How to use

**Requirements:**

* Python 3
* Libraries: `requests` and `beautifulsoup4`

**Running the project:**

Access via terminal:

```bash
python3 main.py
```

If you face any issues on Windows, you may also run it using the `main.bat` file.

---

### Want to contribute?

Planned improvements include:

* Changes in the `Page` class
* Check the HTTP status code directly instead of relying on `raise_status` (see original documentation)
* Add this validation to each method inside the `Page` class
* Add a **Front-End**: remove the current terminal-only dependency in the future (maybe...)
* **Transform the project into an API**

Feel free to open issues or submit pull requests!

<img width="979" height="479" alt="image" src="https://github.com/user-attachments/assets/21735494-60bc-4c61-8617-74d005df0657" />


---

## **Português**

## Sobre este projeto

Ultimamente, tenho precisado baixar alguns arquivos do [archive.org](https://archive.org) e decidi pôr em prática meus estudos recentes: criei um pequeno script para facilitar minha tarefa, gerando os links de download diretamente no terminal.

O uso é simples: **basta colar o link da página do item desejado do site [archive.org](https://archive.org)**.

Porém, decidi deixá-lo aberto e livre! Ficaria lisonjeado caso queira contribuir—sinta-se à vontade para enviar Pull Requests ou fazer forks.
Só tenha uma coisa em mente: este é um código colaborativo que pode ser usado como desejar, mas ele continuará sendo software livre sob a licença GNU GPL v3.

### Sobre a licença GNU GPL v3

A GNU General Public License v3 (GPLv3) é uma licença de software livre que garante:

* Liberdade para usar, modificar e compartilhar o software.
* Qualquer versão modificada distribuída também deve estar sob a GPLv3.

Para saber mais, leia a documentação oficial:
[https://www.gnu.org/licenses/gpl-3.0.pt-br.html](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)

### Como usar

**Requisitos:**

* Python 3
* Bibliotecas: `requests` e `beautifulsoup4`

**Executando o projeto:**

Acesse pelo terminal:

```bash
python3 main.py
```

Caso enfrente dificuldades no Windows, também é possível executar o arquivo `main.bat`.

---

### Deseja contribuir?

As próximas atualizações planejadas são:

* Alterações na classe `Page`
* Checar o status HTTP diretamente em vez de usar `raise_status` (ver a documentação original)
* Adicionar essa verificação em cada método da classe `Page`
* Adicionar um **Front-End**: remover a dependência atual de ser apenas via terminal (no futuro, talvez...)
* **Transformar o projeto em uma API**

Sinta-se livre para abrir *issues* ou enviar *pull requests*!

<img width="979" height="479" alt="image" src="https://github.com/user-attachments/assets/037354bd-c0f5-4e22-9095-961957a5b2ce" />

