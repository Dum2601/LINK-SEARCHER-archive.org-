from flask import Flask, jsonify, request
import json
from get_page import main
# from get_page import page

app = Flask(__name__)



# Rotas para serem criadas:
# -buscar link
# Listar os links
# devolve um Json com os links


@app.route('/')
def health_check():
    return 'Funcionando'

@app.route('/get_link_page', methods=['POST'])
def get_page_link():
    data = request.get_json()
    link = data.get('link')

    if not link:
        return jsonify({"error": "Missing 'link' in request"}), 400

    download_links = main(link)

    return jsonify({"links": download_links})

    



    # Fluxo -> 
    # Recebe o link
    # Se for válido: lista os links



if __name__ == "__main__":
    app.run(debug=True)