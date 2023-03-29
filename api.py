
#    * [] create the front end
#    * [] think about data visiulisation from the csv files statistics/
#    * [] find a team member

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'equipment_monitoring'

# Initialize MySQL
mysql = MySQL(app)
row_headers = ['id', 'date', 'devices', 'destination', 'commune_sce', 'dp_div', 'aref_dir', 'observation', 'livre_par', 'receptionne_par', 'fonction', 'demande', 'telephone', 'email', 'photos_avant', 'photos_apres']

# Route to create a new distribution
@app.route('/distributions', methods=['POST'])
def create_distribution():
    cur = mysql.connection.cursor()
    date = request.json['date']
    commune_sce = request.json['commune_sce']
    dp_div = request.json['dp_div']
    aref_dir = request.json['aref_dir']
    observation = request.json['observation']
    cur.execute("INSERT INTO distributions (date, commune_sce, dp_div, aref_dir, observation) VALUES (%s, %s, %s, %s, %s)",
                (date, commune_sce, dp_div, aref_dir, observation))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Distribution created successfully'})

# Route to get all distributions
@app.route('/distributions', methods=['GET'])
def get_distributions():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM distributions")
    data = cur.fetchall()
    cur.close()
    return jsonify({'message': 'All distributions retrieved successfully', 'distributions': data})

# Route to get a distribution by ID
@app.route('/distributions/<int:distribution_id>', methods=['GET'])
def get_distribution_by_id(distribution_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM distributions WHERE distribution_id= %s", (distribution_id,))
    data = cur.fetchone()
    cur.close()
    if data:
        return jsonify({'message': 'Distribution retrieved successfully', 'distributions': data})
    else:
        return jsonify({'message': 'Distribution not found'}), 404

# Route to update a distribution by ID
@app.route('/distributions/<int:distribution_id>', methods=['PUT'])
def update_distribution(distribution_id):
    cur = mysql.connection.cursor()
    date = request.json['date']
    commune_sce = request.json['commune_sce']
    dp_div = request.json['dp_div']
    aref_dir = request.json['aref_dir']
    observation = request.json['observation']
    cur.execute("UPDATE distributions SET date = %s, commune_sce = %s, dp_div = %s, aref_dir = %s, observation = %s WHERE distribution_id = %s",
                (date, commune_sce, dp_div, aref_dir, observation, distribution_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Distribution updated successfully'})

# Route to delete a distribution by ID
@app.route('/distributions/<int:distribution_id>', methods=['DELETE'])
def delete_distribution(distribution_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM distributions WHERE distribution_id = %s", (distribution_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Distribution deleted successfully'})

# Route to create a new device for a distribution by ID
@app.route('/distributions/<int:distribution_id>/devices', methods=['POST'])
def create_device(distribution_id):
    cur = mysql.connection.cursor()
    name = request.json['name']
    ref = request.json['ref']
    destination = request.json['destination']
    cycle = request.json['cycle']
    fonction =request.json['fonction']
    demande = request.json['demande']
    cur.execute("INSERT INTO devices (distribution_id,name, ref, destination, cycle, fonction, demande) VALUES (%s ,%s, %s, %s, %s, %s, %s)",
                (distribution_id,name, ref, destination, cycle, fonction, demande))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Device created successfully'})

# Route to get all devices for a distribution by ID
@app.route('/distributions/<int:distribution_id>/devices', methods=['GET'])
def get_devices(distribution_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM devices WHERE distribution_id = %s", (distribution_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify({'message': 'All devices retrieved successfully', 'data': data})

# Route to get a device by ID
@app.route('/distributions/<int:distribution_id>/devices/<int:device_id>', methods=['GET'])
def get_device_by_id(distribution_id, device_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM devices WHERE distribution_id = %s AND device_id = %s", (distribution_id, device_id))
    data = cur.fetchone()
    cur.close()
    if data:
        return jsonify({'message': 'Device retrieved successfully', 'data': data})
    else:
        return jsonify({'message': 'Device not found'}), 404

# Route to update a device by ID
@app.route('/distributions/<int:distribution_id>/devices/<int:device_id>', methods=['PUT'])
def update_device(distribution_id, device_id):
    cur = mysql.connection.cursor()
    name = request.json['ref']
    ref = request.json['ref']
    destination = request.json['destination']
    cycle = request.json['cycle']
    fonction =request.json['fonction']
    demande = request.json['demande']
    cur.execute("UPDATE devices SET name = %s, ref = %s, destination = %s, cycle = %s, fonction = %s, demande = %s WHERE distribution_id = %s AND device_id = %s",
                (name, ref, destination, cycle, fonction, demande, distribution_id, device_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Device updated successfully'})

# Route to delete a device by ID
@app.route('/distributions/<int:distribution_id>/devices/<int:device_id>', methods=['DELETE'])
def delete_device(distribution_id, device_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM devices WHERE distribution_id = %s AND device_id = %s", (distribution_id, device_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Device deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

