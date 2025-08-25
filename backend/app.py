from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection (replace with your URI)
client = MongoClient("")
db = client["todoDB"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.get_json()
    item_name = data.get("itemName")
    item_desc = data.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"error": "Missing fields"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({"message": "To-Do Item submitted successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
