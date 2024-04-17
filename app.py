from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Usuario1", "cpf": "12345", "age": "1"},
    {"id": 2, "nome": "Usuario2", "cpf": "123456", "age": "2"},
    {"id": 3, "nome": "Usuario3", "cpf": "1234567", "age": "3"},
    {"id": 4, "nome": "Usuario4", "cpf": "12345678", "age": "4"},
    {"id": 5, "nome": "Usuario5", "cpf": "123456789", "age": "5"}
]

@app.route('/cadastrarusuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    novo_id = dados.get('id')
    novo_nome = dados.get('nome')
    novo_cpf = dados.get('cpf')
    nova_age = dados.get('age')


    if novo_id and novo_nome:
        for usuario in usuarios:
            if usuario["id"] == novo_id:
                return jsonify({"erro": "ID já existe"}), 400

        novo_usuario = {"id": novo_id, "nome": novo_nome, "cpf": novo_cpf, "age": nova_age}
        usuarios.append(novo_usuario)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    else:
        return jsonify({"erro": "Dados inválidos"}), 400 

@app.route('/alterarusuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()
    novo_nome = dados.get('nome')
    novo_cpf = dados.get('cpf')
    nova_age = dados.get('age')

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = novo_nome
            usuario["cpf"] = novo_cpf
            usuario["age"] = nova_age

            return jsonify({"mensagem": "Usuário atualizado com sucesso!"}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/deletarusuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return jsonify({"mensagem": "Usuário excluído com sucesso!"}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify({"usuario": usuario}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/atualizarusuario/<int:id>', methods=['PATCH'])
def atualizar_dados_usuario(id):
    dados = request.get_json()
    novo_nome = dados.get('nome')
    novo_cpf = dados.get('cpf')

    for usuario in usuarios:
        if usuario["id"] == id:
            if novo_nome:
                usuario["nome"] = novo_nome
                usuario["cpf"] = novo_cpf
            return jsonify({"mensagem": "Dados do usuário atualizados com sucesso!"}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == '__main__':
    app.run(debug=True)