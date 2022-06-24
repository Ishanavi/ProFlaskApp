from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Contact': '9887564345',
        'Name': 'Alex', 
        'done': False
    },
    {
        'id': 2,
        'Contact': '9893456434',
        'Name': 'Justin', 
        'done': False
    }
]


@app.route("/add-contacts", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-contact")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)