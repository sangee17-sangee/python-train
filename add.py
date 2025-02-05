from flask import Flask, request, jsonify

app = Flask(__name__)

menu = []  #strings

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify({'menu': menu}), 200

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()

    if not data or not data.get('name'):
        return jsonify({"error": "Missing 'name' in request data"}), 400

    name = data['name']

    menu.append(name)  # adding list
    return jsonify({
        "message": "Item added successfully",
        "item": name  # actual name
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
