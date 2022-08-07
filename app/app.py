from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from marshmallow import Schema, fields, ValidationError


class Findings(Schema):
    researcher_email = fields.String(required=True)
    species_id = fields.String(required=True)
    location = fields.String(required=True)
    finding_date = fields.DateTime(required=True)
    notes = fields.String()


app = Flask(__name__)

db_name = 'species'
db_user = 'recep'
db_pass = '342516'
db_host = 'species'
db_port = '5432'


db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

@app.route("/")
def hello_world():
    return "This is Catalog of Life API!"

@app.route("/search", methods=['GET'])
def search():
    try:
        args = request.args
        name_param = args.get("name")
        query = """SELECT ID, scientificName FROM NameUsage WHERE 
                scientificName like '%%{search}%%';""".format(search=name_param)
        print(query)
        result_proxy = db.execute(query)
        result = result_proxy.fetchall()

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify({'result': [dict(row) for row in result]})

@app.route("/search_all", methods=['GET'])
def search_all():
    try:
        args = request.args
        name_param = args.get("name")
        query = """SELECT * FROM NameUsage WHERE 
                scientificName like '%%{search}%%';""".format(search=name_param)
        print(query)
        result_proxy = db.execute(query)
        result = result_proxy.fetchall()

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify({'result': [dict(row) for row in result]})

@app.route("/search_by_id", methods=['GET'])
def search_by_id():
    try:
        args = request.args
        species_id = args.get("ID")
        query = """SELECT * FROM NameUsage WHERE 
                scientificName ID'{}';""".format(species_id)
        print(query)
        result_proxy = db.execute(query)
        result = result_proxy.fetchall()

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify({'result': [dict(row) for row in result]})

@app.route("/get_findings", methods=['GET'])
def get_findings():
    try:
        args = request.args
        species_id = args.get("species_id")
        query = """SELECT 
                researcherEmail, 
                findingDate, 
                location,
                notes 
                FROM Findings WHERE 
                speciesID = '{}';""".format(species_id)

        result_proxy = db.execute(query)
        result = result_proxy.fetchall()

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify({'result': [dict(row) for row in result]})



@app.route("/record_species", methods=["POST"])
def record_species():

    try:
        input = request.get_json(force=True)

        findings_schema = Findings()
        model_result = findings_schema.load(input)

        query = """INSERT INTO Findings(speciesID, researcherEmail, findingDate, location, notes) 
        VALUES('{}','{}','{}','{}','{}')
        """.format(
        model_result.get('species_id'), 
        model_result.get('researcher_email'), 
        model_result.get('finding_date'),
        model_result.get('location'), 
        model_result.get('notes'))

        db.execute(query) 

    except ValidationError as err:
        return jsonify(err.messages), 400

  
    dictToReturn = {'result': 'SUCCESS'}
    return jsonify(dictToReturn)

@app.route("/post", methods=["POST"])
def testsend():
    input = request.get_json(force=True)
    dictToReturn = {'foo': input['text']}
    return jsonify(dictToReturn)


if __name__ == "__main__":
    app.run(debug=True)
