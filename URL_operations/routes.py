from flask import Flask, jsonify, request
from get_page import main

app = Flask(__name__)

# Variável global para armazenar os últimos links obtidos
download_links = []

@app.route('/')
def health_check():
    return 'Funcionando'

@app.route('/get_link_page', methods=['POST'])
def get_page_link():
    data = request.get_json()
    if not data or 'link' not in data:
        return jsonify({"error": "Missing 'link' in request"}), 400

    link = data['link']
    global download_links
    download_links = main(link)  # Pega os links da função main
    return jsonify({"message": "Links obtained successfully", "links": download_links})

@app.route('/list_links', methods=['GET'])
def list_links():
    return jsonify({"links": download_links})
    

if __name__ == "__main__":
    app.run(debug=True)

    



    # Fluxo -> 
    # Recebe o link OK
    # Se for válido: lista os links OK

