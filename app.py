### ADD THIS LATER 

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'equipment_monitoring'

mysql = MySQL(app)

# GET equipment
@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM equipment")
    results = cur.fetchall()
    cur.close()
    return jsonify(results)


# POST equipment
@app.route('/equipment', methods=['POST'])
def create_equipment():
    date = request.json['date']
    unite_centrale = request.json['unite_centrale']
    ecran = request.json['ecran']
    printer = request.json['printer']
    video_projecteur = request.json['video_projecteur']
    destination = request.json['destination']
    cycle = request.json['cycle']
    livre_par = request.json['livre_par']
    receptionne_par = request.json['receptionne_par']
    fonction = request.json['fonction']
    demande = request.json['demande']
    telephone = request.json['telephone']
    email = request.json['email']
    photos_avant = request.json['photos_avant']
    photos_apres = request.json['photos_apres']
    commune = request.json['commune']
    DP = request.json['DP']
    AREF = request.json['AREF']
    observation = request.json['observation']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO equipment (date, unite_centrale, ecran, printer, video_projecteur, destination, cycle, livre_par, receptionne_par, fonction, demande, telephone, email, photos_avant, photos_apres, commune, DP, AREF, observation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, unite_centrale, ecran, printer, video_projecteur, destination, cycle, livre_par, receptionne_par, fonction, demande, telephone, email, photos_avant, photos_apres, commune, DP, AREF, observation))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Equipment record created successfully."})

# PUT equipment
@app.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    date = request.json['date']
    unite_centrale = request.json['unite_centrale']
    ecran = request.json['ecran']
    printer = request.json['printer']
    video_projecteur = request.json['video_projecteur']
    destination = request.json['destination']
    cycle = request.json['cycle']
    livre_par = request.json['livre_par']
    receptionne_par = request.json['receptionne_par']
    fonction = request.json['fonction']
    demande = request.json['demande']
    telephone = request.json['telephone']
    email = request.json['email']
    photos_avant = request.json['photos_avant']
    photos_apres = request.json['photos_apres']
    commune = request.json['commune']
    DP = request.json['DP']
    AREF = request.json['AREF']
    observation = request.json['observation']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE equipment SET date=%s, unite_centrale=%s, ecran=%s, printer=%s, video_projecteur=%s, destination=%s, cycle=%s, livre_par=%s, receptionne_par=%s, fonction=%s, demande=%s, telephone=%s, email=%s, photos_avant=%s, photos_apres=%s, commune=%s, DP=%s, AREF=%s, observation=%s WHERE id=%s", (date, unite_centrale, ecran, printer, video_projecteur, destination, cycle, livre_par, receptionne_par, fonction, demande, telephone, email, photos_avant, photos_apres, commune, DP, AREF, observation, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Equipment record updated successfully."})

# DELETE 
@app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM equipment WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Equipment record deleted successfully."})

# GET by id 
@app.route('/equipment/<int:id>', methods=['GET'])
def get_equipment_by_id(id):
    """
    Retrieve a single equipment record by ID.
    """
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM equipment WHERE id = %s", (id,))
        equipment = cursor.fetchone()
        cursor.close()
        if equipment:
            # Convert the equipment data to a dictionary for JSON serialization
            equipment_dict = {
                'id': equipment[0],
                'date': equipment[1],
                'unite_centrale': equipment[2],
                'ecran': equipment[3],
                'printer': equipment[4],
                'video_projecteur': equipment[5],
                'destination': equipment[6],
                'cycle': equipment[7],
                'livre_par': equipment[8],
                'receptionne_par': equipment[9],
                'fonction': equipment[10],
                'demande': equipment[11],
                'telephone': equipment[12],
                'email': equipment[13],
                'photos_avant': equipment[14],
                'photos_apres': equipment[15],
                'commune': equipment[16],
                'DP': equipment[17],
                'AREF': equipment[18],
                'observation': equipment[19]
            }
            # Return the equipment data as JSON
            return jsonify(equipment_dict), 200
        else:
            # Return a 404 error if the equipment record doesn't exist
            return jsonify({'error': 'Equipment not found.'}), 404
    except Exception as e:
        # Return a 500 error if there was a problem with the database query
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
