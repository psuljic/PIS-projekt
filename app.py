from flask import Flask, g, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('./database.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite3_db.close()

@app.route('/')
def index():
    return '<h1>Gifty App</h1>'

#GET ALL
@app.route('/wishlist')
def viewwishlist():
    db = get_db()
    cursor = db.execute('SELECT * FROM wishlist')
    results = []
    for result in cursor.fetchall():
        result_dict = {}
        for i, col in enumerate(cursor.description):
            result_dict[col[0]] = result[i]
        results.append(result_dict)
    return jsonify(results)

#CREATE
@app.route('/wishlist', methods=['POST'])
def add_item():
    db = get_db()
    name = request.json['name']
    link = request.json['link']
    db.execute('INSERT INTO wishlist (name, link) VALUES (?,?)', [name, link])
    db.commit()
    return jsonify({'message': 'Item added successfully!'})

#GET ONE 
@app.route('/wishlist/<int:item_id>', methods=['GET'])
def get_item(item_id):
    db = get_db()
    cursor = db.execute('SELECT * FROM wishlist WHERE id = ?', [item_id])
    result = cursor.fetchone()
    if not result:
        return jsonify({'error': 'Item not found'})
    #return f"<h1>The Id is {result['id']}. <br>The Name is {result['name']}."
    return jsonify({'id': result['id'], 'name': result['name'], 'link': result['link']})

#UPDATE
@app.route('/wishlist/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    db = get_db()
    name = request.json['name']
    link = request.json['link']
    db.execute('UPDATE wishlist SET name = ?, link = ? WHERE id = ?', [name, link, item_id])
    db.commit()
    return jsonify({'message': 'Item updated successfully'})

#DELETE
@app.route('/wishlist/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db = get_db()
    db.execute('DELETE FROM wishlist WHERE id = ?', [item_id])
    db.commit()
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)