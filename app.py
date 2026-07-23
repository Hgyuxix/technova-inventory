from flask import Flask, jsonify, request

app = Flask(__name__)

# Data inventaris sementara (in-memory)
inventory = [
    {"id": 1, "name": "Laptop", "quantity": 10},
    {"id": 2, "name": "Mouse", "quantity": 50},
]

@app.route("/")
def home():
    return jsonify({"message": "TechNova Inventory API is running"})

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory)

@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.get_json()
    new_item["id"] = len(inventory) + 1
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)