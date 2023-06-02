#pip intall flask
#pip install requests
from flask import Flask

app = Flask(__name__)

@app.route('/bemvindo', methods=['GET'])
def sejaBemVindoGET():
    return 'Hello World'

@app.route('/bemvindo', methods=['POST'])
def sejaBemVindoPOST():
    return 'Cadastrar Hello World'

@app.route('/bemvindo', methods=['PUT'])
def sejaBemVindoPUT():
    return 'Atualizar Hello World'

@app.route('/bemvindo', methods=['DELETE'])
def sejaBemVindoDELETE():
    return 'Deletar Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 105)

